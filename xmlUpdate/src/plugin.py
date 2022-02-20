#!/usr/bin/python
# -*- coding: utf-8 -*-

# for localized messages
from . import _
import urllib.request, urllib.error, urllib.parse
from Components.ActionMap import ActionMap
from Components.config import config, ConfigSelection, getConfigListEntry
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Plugins.Plugin import PluginDescriptor
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Screens.Standby import TryQuitMainloop

config.dvbtypexmlupdate = ConfigSelection(default="satellites", choices=[("atsc", _("ATSC")), ("cables", _("Cables")), ("satellites", _("Satellites")), ("terrestrial", _("Terrestrial")), ("unicable", _("Unicable"))])
config.satellitestypexmlupdate = ConfigSelection(default="europe", choices=[("all", _("All (not recommended)")), ("america", _("America (61°W-160°W)")), ("asia", _("Asia (160°W-73°E)")), ("atlantic", _("Atlantic (0°W-61°W)")), ("europe", _("Europe (73°E-0°E)"))])
config.foldertypexmlupdate = ConfigSelection(default="/etc/tuxbox", choices=[("/etc/tuxbox", _("/etc/tuxbox (default)")), ("/etc/enigma2", _("/etc/enigma2")), ("/usr/share/enigma2", _("/usr/share/enigma2 (default for unicable)"))])


class xmlUpdate(ConfigListScreen, Screen):
	def __init__(self, session):
		Screen.__init__(self, session)
		self.setup_title = _("XML update for Open Vision")
		Screen.setTitle(self, self.setup_title)
		self.skinName = ["xmlUpdate", "Setup"]
		self.session = session
		ConfigListScreen.__init__(self, [], session=self.session)

		self.DVBtype = config.dvbtypexmlupdate
		self.Satellitestype = config.satellitestypexmlupdate
		self.folder = config.foldertypexmlupdate

		self["actions"] = ActionMap(["SetupActions", "ColorActions"],
		{
			"ok": self.keyGo,
			"cancel": self.keyCancel,
			"back": self.keyCancel,
			"save": self.keyGo,
			"green": self.keyGo,
			"yellow": self.keySave,
		}, -2)

		self["key_red"] = StaticText(_("Exit"))
		self["key_green"] = StaticText(_("Fetch"))
		self["key_yellow"] = StaticText(_("Save"))

		self["description"] = Label("")

		self.createSetup()

		if not self.selectionChanged in self["config"].onSelectionChanged:
			self["config"].onSelectionChanged.append(self.selectionChanged)
		self.selectionChanged()

	def selectionChanged(self):
		self["description"].setText(self.getCurrentDescription())

	def createSetup(self):
		self.list = []

		self.list.append(getConfigListEntry(_("Fetch"), self.DVBtype, _('File being updated, i.e. satellites.xml')))
		if self.DVBtype.value == "satellites":
			self.list.append(getConfigListEntry(_("Region"), self.Satellitestype, _('Choose where you live.')))
		self.list.append(getConfigListEntry(_("Save to"), self.folder, _('Folder where the downloaded file will be saved. "/etc/tuxbox" is the default location. Files stored in "/etc/enigma2" override the default file and are not updated on a software update.')))

		self["config"].list = self.list
		self["config"].l.setList(self.list)

	def keySave(self):
		for x in self["config"].list:
			x[1].save()
			self.close()

	def keyGo(self):
		XMLdata = self.fetchURL()
		if XMLdata:
			if self.validXML(XMLdata):
				try:
					with open(self.folder.value + "/" + self.DVBtype.value + ".xml", "w") as f:
						f.write(XMLdata)
						f.close()
				except IOError as err:
					print("[xmlUpdate][keyGo] Saving file failed.", err)
					self.showError(_("Saving the %s.xml file failed") % self.DVBtype.value)
				else:
					print("[xmlUpdate][keyGo] Saving %s to %s succeeded." % (self.DVBtype.value, self.folder.value))
					self.showRestartMessage(_("Fetching and saving %s.xml succeeded.\nRestart now for changes to take immediate effect?") % self.DVBtype.value)
			else: # XML did not validate
				print("[xmlUpdate][validXML] Closing documentElement missing.")
				self.showError(_("The %s.xml download was corrupt.") % self.DVBtype.value)

	def keyCancel(self):
		self.close()

	def fetchURL(self):
		if self.DVBtype.value == "satellites":
			if self.Satellitestype.value != "all":
				self.url = "https://raw.githubusercontent.com/OpenVisionE2/openvision-xml/master/xml/satellites-%s.xml"
				print('[xmlUpdate][fetchURL] URL', self.url % self.Satellitestype.value)
			else:
				self.url = "https://raw.githubusercontent.com/OpenVisionE2/openvision-xml/master/xml/%s.xml"
				print('[xmlUpdate][fetchURL] URL', self.url % self.DVBtype.value)
		else:
			self.url = "https://raw.githubusercontent.com/OpenVisionE2/openvision-xml/master/xml/%s.xml"
			print('[xmlUpdate][fetchURL] URL', self.url % self.DVBtype.value)
		try:
			if self.DVBtype.value == "satellites":
				if self.Satellitestype.value != "all":
					req = urllib.request.Request(self.url % self.Satellitestype.value)
				else:
					req = urllib.request.Request(self.url % self.DVBtype.value)
			else:
				req = urllib.request.Request(self.url % self.DVBtype.value)
			response = urllib.request.urlopen(req)
			print('[xmlUpdate][fetchURL] Response: %d' % response.getcode())
			if int(response.getcode()) == 200:
				return response.read()
		except urllib.error.HTTPError as err:
			print('[xmlUpdate][fetchURL] ERROR:', err)
		except urllib.error.URLError as err:
			print('[xmlUpdate][fetchURL] ERROR:', err.reason[0])
		except urllib2 as err:
			print('[xmlUpdate][fetchURL] ERROR:', err)
		except:
			import sys
			print('[xmlUpdate][fetchURL] undefined error', sys.exc_info()[0])
		self.showError(_("The %s.xml file could not be fetched") % self.DVBtype.value)

	def validXML(self, XMLdata): # Looks for closing documentElement, i.e. </satellites>, </cables>, or </locations>
		return self.DVBtype.value in ('satellites', 'cables', 'unicable') and ("</%s>" % self.DVBtype.value) in XMLdata or self.DVBtype.value in ('terrestrial', 'atsc') and "</locations>" in XMLdata

	def showError(self, message):
		mbox = self.session.open(MessageBox, message, MessageBox.TYPE_ERROR)
		mbox.setTitle(_("XML update"))

	def showRestartMessage(self, message):
		mbox = self.session.openWithCallback(self.restartGUI, MessageBox, message, MessageBox.TYPE_YESNO)
		mbox.setTitle(_("XML update"))

	def restartGUI(self, answer=None):
		if answer:
			self.session.open(TryQuitMainloop, 3)


def xmlUpdateStart(menuid, **kwargs):
	if menuid == "scan":
		return [(_("XML update"), xmlUpdateMain, "xmlUpdate", 70)]
	return []


def xmlUpdateMain(session, **kwargs):
	session.open(xmlUpdate)


def Plugins(**kwargs):
	pList = []
	pList.append(PluginDescriptor(name=_("XML update"), description="For undating transponder xml files", where=PluginDescriptor.WHERE_MENU, needsRestart=False, fnc=xmlUpdateStart))
	return pList
