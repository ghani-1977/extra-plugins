#!/usr/bin/python
# -*- coding: utf-8 -*-

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
import os
from enigma import eTimer
#########


class LoopSyncMain(Screen):
	def __init__(self, session, args=None):
		Screen.__init__(self, session)
		self.session = session
		self.gotSession()

	def gotSession(self):
		self.stopped = 0
		self.ResetFlag()
		self.AVSyncTimer = eTimer()
		self.AVSyncTimer.callback.append(self.UpdateStatus)
		self.AVSyncTimer.start(10000, True)

	def UpdateStatus(self):
		if self.stopped == 1:
			try:
				self.session.open(DoReZap, self.srv)
			except Exception as e:
				print("[ReZap] Can't Zap")
			self.stopped = 0
			self.AVSyncTimer.start(100, True)
			return
		frontendDataOrg = ""
		#self.srv = self.session.nav.getCurrentlyPlayingServiceOrGroup()
		self.srv = self.session.nav.getCurrentlyPlayingServiceReference()
		if self.srv:
			service = self.session.nav.getCurrentService()
			if service:
				feinfo = service.frontendInfo()
				frontendDataOrg = feinfo and feinfo.getAll(True)
				if frontendDataOrg:		### DVB-S/C/T ###
					if self.CheckFlag():
						print("[ReZap] DoReZap !!!")
						self.ResetFlag()
						self.session.nav.stopService()
						self.session.nav.playService(None)
						self.stopped = 1
						self.AVSyncTimer.start(10, True)
					self.AVSyncTimer.start(100, True)
					return
				else:		### IPTV or VOD ###
					self.ResetFlag()
					self.AVSyncTimer.start(500, True)
					return
			else:
				self.AVSyncTimer.start(500, True)
				return
		else:
			### NoService ###
			self.AVSyncTimer.start(500, True)
			return

	def CheckFlag(self):
		try:
			print("[ReZap] Read /sys/class/tsync/reset_flag")
			if int(open("/sys/class/tsync/reset_flag", "r").read(), 16) == 1:
				return True
		except Exception as e:
			print("[ReZap] Read /sys/class/tsync/reset_flag failed.")
			self.AVSyncTimer.start(500, True)
		return False

	def ResetFlag(self):
		try:
			print("[ReZap] Write to /sys/class/tsync/reset_flag")
			open("/sys/class/tsync/reset_flag", "w").write("0")
		except Exception as e:
			print("[ReZap] Write to /sys/class/tsync/reset_flag failed.")

###################################


class DoReZap(Screen):

	skin = """
		<screen position="center,center" size="1920,1080" title="" >
		</screen>"""

	def __init__(self, session, xxx):
		Screen.__init__(self, session)

		try:
			print("[ReZap] Read /sys/class/video/blackout_policy")
			open("/sys/class/video/blackout_policy", "w").write("0")
		except Exception as e:
			print("[ReZap] Read /sys/class/video/blackout_policy failed.")
		self.session.nav.playService(xxx)
		try:
			print("[ReZap] Write to /sys/class/video/blackout_policy")
			open("/sys/class/video/blackout_policy", "w").write("1")
		except Exception as e:
			print("[ReZap] Write to /sys/class/video/blackout_policy failed.")
		self.close()


###################################

def sessionstart(session, **kwargs):
	session.open(LoopSyncMain)


def Plugins(**kwargs):
	return [
		PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionstart)
		]
