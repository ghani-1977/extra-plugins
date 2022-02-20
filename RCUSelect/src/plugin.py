#!/usr/bin/python
# -*- coding: utf-8 -*-

# for localized messages
from . import _
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Plugins.Plugin import PluginDescriptor
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.Button import Button
from Components.SystemInfo import BoxInfo
import os
from Components.Console import Console
from Tools.Directories import resolveFilename, SCOPE_PLUGINS


class RCUSelect(Screen):
	skin = """
	<screen name="Menusimple" position="center,center" size="600,475" title="" >
	<widget name="list" position="30,30" size="490,370" scrollbarMode="showOnDemand" />
	<widget name="info" position="75,5" zPosition="4" size="330,340" font="Regular;18" foregroundColor="#ffffff" transparent="1" halign="left" valign="center" />
	<ePixmap name="red"    position="20,425"   zPosition="2" size="140,40" pixmap="buttons/red.png" transparent="1" alphatest="on" />
	<ePixmap name="green"  position="190,425" zPosition="2" size="140,40" pixmap="buttons/green.png" transparent="1" alphatest="on" />
	<widget name="key_red" position="20,425" size="140,40" valign="center" halign="center" zPosition="4"  foregroundColor="white" font="Regular;20" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
	<widget name="key_green" position="190,425" size="140,40" valign="center" halign="center" zPosition="4"  foregroundColor="white" font="Regular;20" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
	</screen>"""

	def __init__(self, session, args=0):
		self.session = session
		Screen.__init__(self, session)
		self.skinName = "RCUSelect"
		self.index = 0
		self.rcuval = []
		self.rcuvalOSD = []
		self["actions"] = ActionMap(["OkCancelActions", "ColorActions"],
		{
			"ok": self.action,
			"cancel": self.close,
			"red": self.close,
			"green": self.action,
		}, -1)
		self["key_green"] = Button(_("Apply"))
		self["key_red"] = Button(_("Cancel"))

		self.testlist = []
		self["info"] = Label()
		self["list"] = MenuList(self.rcuvalOSD)
		title = _("RCU Select")
		self.setTitle(title)
		self["pixmap"] = Pixmap()
		self.rcuval = [_("A400 NEC remote"),
		_("Alien 1 Old HOF54B1-4 remote"),
		_("Alien 2 New HOF55D remote"),
		_("Alien 5 amlogic NEC remote"),
		_("Factory amlogic NEC remote"),
		_("GigaBlue 800 UE Plus remote"),
		_("Golden Interstar LX3 remote"),
		_("K1 Plus amlogic NEC remote"),
		_("K1 Pro amlogic NEC remote"),
		_("M8S ZAP-A10 NEC remote"),
		_("M8S Plus amlogic NEC remote"),
		_("MB2 amlogic M8B remote"),
		_("MX3G amlogic MXIII-G remote"),
		_("MX Pro 2 amlogic MXproII remote"),
		_("MXQV20 ZAP-A10 NEC remote"),
		_("MXQV31 amlogic NEC remote"),
		_("Octagon SF8 remote"),
		_("Qintex Q812 remote"),
		_("CVT RC5 remote"),
		_("RCMM amlogic NEC remote"),
		_("TX1 amlogic NEC remote"),
		_("TX3 Pro amlogic NEC remote"),
		_("TX5 Pro amlogic NEC remote"),
		_("Vander amlogic remote"),
		_("Wechip V5 amlogic remote"),
		_("WeTek Play NEC remote"),
		_("WeTek Play (Classic) remote"),
		_("WeTek Play Enigma2 remote"),
		_("WeTek OpenELEC NEC remote"),
		_("Xtrend ET10000 remote"),
		_("Mutant HD2400 remote"),
		_("AB IPBox 9900/99/55HD remote"),
		_("WeTek Play 2 NEC remote"),
		_("Technomate Nano remote"),
		_("X96 amlogic remote"),
		_("X98 amlogic remote"),
		_("Zgemma Star remote")]
		self.SetOSDList()
		self.MakeKeymapBckUp()

	def MakeKeymapBckUp(self):
		filename = resolveFilename(SCOPE_PLUGINS, "Extensions/RCUSelect/conf/keymap.orig.xml")
		cmd = "cp -f /usr/share/enigma2/keymap.xml " + filename + " &"
		if not os.path.exists(filename):
			Console().ePopen(cmd)

	def SetOSDList(self):
		choice = "WeTek Play Enigma2 remote"
		try:
			choice = open("/etc/amremote/rcuselect-choice", "r").read()
		except IOError:
			pass
		self.rcuold = choice
		for x in self.rcuval:
			if x == choice:
				self.rcuvalOSD.append(x + "  -  SET")
			else:
				self.rcuvalOSD.append(x)
		self["list"].setList(self.rcuvalOSD)

	def action(self):
		from Screens.MessageBox import MessageBox
		self.session.openWithCallback(self.confirm, MessageBox, _("Are you sure?"), MessageBox.TYPE_YESNO, timeout=15, default=False)

	def confirm(self, confirmed):
		if not confirmed:
			print("not confirmed")
			self.close()
		else:
			var = self["list"].getSelectionIndex()
			self.rcuv = self.rcuval[var]
			#if self.rcuv != self.rcuold: copy keymap
			try:
				if self.rcuv == "A400 NEC remote":
					Console().ePopen("cp -f /etc/amremote/a400.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Alien 1 Old HOF54B1-4 remote":
					Console().ePopen("cp -f /etc/amremote/alien.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Alien 2 New HOF55D remote":
					Console().ePopen("cp -f /etc/amremote/alien2.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Alien 5 amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/alien5.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Factory amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/factory_remote.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "GigaBlue 800 UE Plus remote":
					Console().ePopen("cp -f /etc/amremote/gb800ueplus.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Golden Interstar LX3 remote":
					Console().ePopen("cp -f /etc/amremote/gilx3.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "K1 Plus amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/k1plus.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "K1 Pro amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/k1pro.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "M8S ZAP-A10 NEC remote":
					Console().ePopen("cp -f /etc/amremote/m8s.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "M8S Plus amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/m8splus.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "MB2 amlogic M8B remote":
					Console().ePopen("cp -f /etc/amremote/mb2.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "MX3G amlogic MXIII-G remote":
					Console().ePopen("cp -f /etc/amremote/mx3g.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "MX Pro 2 amlogic MXproII remote":
					Console().ePopen("cp -f /etc/amremote/mxpro2.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "MXQV20 ZAP-A10 NEC remote":
					Console().ePopen("cp -f /etc/amremote/mxqv20.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "MXQV31 amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/mxqv31.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Octagon SF8 remote":
					Console().ePopen("cp -f /etc/amremote/octagonsf8.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Qintex Q812 remote":
					Console().ePopen("cp -f /etc/amremote/qintex.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "CVT RC5 remote":
					Console().ePopen("cp -f /etc/amremote/rc5.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "RCMM amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/remotercmm.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "TX1 amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/tx1.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "TX3 Pro amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/tx3pro.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "TX5 Pro amlogic NEC remote":
					Console().ePopen("cp -f /etc/amremote/tx5pro.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Vander amlogic remote":
					Console().ePopen("cp -f /etc/amremote/vander.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Wechip V5 amlogic remote":
					Console().ePopen("cp -f /etc/amremote/wechipv5.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "WeTek Play NEC remote":
					Console().ePopen("cp -f /etc/amremote/wetek0.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "WeTek Play (Classic) remote":
					Console().ePopen("cp -f /etc/amremote/wetek1.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "WeTek Play Enigma2 remote":
					Console().ePopen("cp -f /etc/amremote/wetek2.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "WeTek OpenELEC NEC remote":
					Console().ePopen("cp -f /etc/amremote/wetek3.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Xtrend ET10000 remote":
					Console().ePopen("cp -f /etc/amremote/wetek_et10000remote.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Mutant HD2400 remote":
					Console().ePopen("cp -f /etc/amremote/wetek_hd2400remote.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "AB IPBox 9900/99/55HD remote":
					Console().ePopen("cp -f /etc/amremote/wetek_ipbox9900remote.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "WeTek Play 2 NEC remote":
					Console().ePopen("cp -f /etc/amremote/wetek_play2.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Technomate Nano remote":
					Console().ePopen("cp -f /etc/amremote/wetek_tmnanoremote.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "X96 amlogic remote":
					Console().ePopen("cp -f /etc/amremote/x96.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "X98 amlogic remote":
					Console().ePopen("cp -f /etc/amremote/x98.conf /etc/amremote/rcuselect.conf &")
				elif self.rcuv == "Zgemma Star remote":
					Console().ePopen("cp -f /etc/amremote/zgemmastar.conf /etc/amremote/rcuselect.conf &")
				else:
					Console().ePopen("cp -f /etc/amremote/wetek2.conf /etc/amremote/rcuselect.conf &")
				open("/etc/amremote/rcuselect-choice", "w").write(self.rcuv)
				Console().ePopen("killall -9 remotecfg &")
				if BoxInfo.getItem("model") == "wetekplay2":
					fin = open("/etc/amremote/rcuselect.conf")
					fout = open("/etc/amremote/rcuselect_tmp.conf", "w")
					for line in fin:
						if "work_mode" in line:
							line = "work_mode  	= 0\n"
						fout.write(line)
					fout.close()
					Console().ePopen("mv -f /etc/amremote/rcuselect_tmp.conf /etc/amremote/rcuselect.conf &")
				Console().ePopen("/usr/bin/remotecfg /etc/amremote/rcuselect.conf &")
				if self.rcuold == "WeTek OpenELEC NEC remote" or self.rcuv == "WeTek OpenELEC NEC remote":
					if self.rcuold != self.rcuv:
						if self.rcuv == "WeTek OpenELEC NEC remote":
							Console().ePopen("cp -f %s /usr/share/enigma2/keymap.xml &") % resolveFilename(SCOPE_PLUGINS, "Extensions/RCUSelect/conf/keymap.OE.xml")
						else:
							Console().ePopen("cp -f %s /usr/share/enigma2/keymap.xml &") % resolveFilename(SCOPE_PLUGINS, "Extensions/RCUSelect/conf/keymap.orig.xml")
						Console().ePopen("killall -9 enigma2 &")
				else:
					Console().ePopen("cp -f %s /usr/share/enigma2/keymap.xml &") % resolveFilename(SCOPE_PLUGINS, "Extensions/RCUSelect/conf/keymap.orig.xml")
			except IOError:
				print("RCU select failed.")
			self.close()

	def cancel(self):
		self.close()


def startConfig(session, **kwargs):
        session.open(RCUSelect)


def system(menuid):
	if menuid == "system":
		return [(_("RCU Select"), startConfig, "RCU Select", None)]
	else:
		return []


def Plugins(**kwargs):
	return PluginDescriptor(name=_("RCU Select"), where=PluginDescriptor.WHERE_MENU, fnc=system)
