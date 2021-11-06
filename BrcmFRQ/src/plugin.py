from __future__ import print_function
from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.Button import Button
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigList
from Components.config import config, configfile, ConfigSubsection, getConfigListEntry, ConfigSelection
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.SystemInfo import BoxInfo
import Screens.Standby
from enigma import eTimer

platform = BoxInfo.getItem("platform")

config.plugins.brcm = ConfigSubsection()
if platform == 'edision4k':
    config.plugins.brcm.governor = ConfigSelection(default='performance', choices=[('powersave', 'powersave'), ('userspace', _('userspace')), ('conservative', 'conservative'), ('ondemand', 'ondemand (suggested)'), ('performance', 'performance (default)')])
    config.plugins.brcm.maxfrq = ConfigSelection(default='1503000', choices=[('300000', '300MHz'), ('501000', '500MHz'), ('751000', '750MHz'), ('1002000', '1.0GHz'), ('1503000', _('1.5GHz (default)'))])
    config.plugins.brcm.minfrq = ConfigSelection(default='300000', choices=[('300000', '300MHz (default)'), ('501000', '500MHz'), ('751000', '750MHz'), ('1002000', '1.0GHz'), ('1503000', _('1.5GHz'))])


def leaveStandby():
    print('[BrcmFRQ] Leave Standby')
    initBooster()


def standbyCounterChanged(configElement):
    print('[BrcmFRQ] In Standby')
    initStandbyBooster()
    from Screens.Standby import inStandby
    inStandby.onClose.append(leaveStandby)


def initBooster():
    print('[BrcmFRQ] initBooster')
    try:
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq', 'w')
        f.write(config.plugins.brcm.maxfrq.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq', 'w')
        f.write(config.plugins.brcm.minfrq.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor', 'w')
        f.write(config.plugins.brcm.governor.getValue())
        f.close()
    except:
        pass


def initStandbyBooster():
    print('[BrcmFRQ] initStandbyBooster')
    try:
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq', 'w')
        f.write(config.plugins.brcm.minfrq.getValue())
        f.close()
    except:
        pass


class BrcmFRQ(ConfigListScreen, Screen):

    def __init__(self, session, args=None):
        self.skin = '\n<screen  position="0,0" size="1920,1080" title="CPU Frequency Setup" flags="wfNoBorder" backgroundColor="FNCScreenBackground">\n        <widget source="Title" render="Label" position="210,140" size="1500,68" zPosition="2" halign="center" font="Regular; 36" backgroundColor="FNCmainColor" transparent="1" valign="center" />\n        <ePixmap name="bPPodloga" position="210,140" size="1500,820" pixmap="Estuary/background/back_mon_empty.png" zPosition="-10" />\n        <eLabel name="" position="235,227" size="1283,648" zPosition="-5" />\n        <ePixmap pixmap="Estuary/menu/icons/fw.png" position="1567,284" size="90,70" zPosition="1" />\n        <eLabel name="" position="1542,435" size="145,50" font="Regular; 28" valign="center" halign="center" text="Exit" />\n        <ePixmap pixmap="Estuary/buttons/buttons.png" position="214,893" size="1100,56" alphatest="blend" zPosition="100" />\n\n        <widget name="key_red" position="235,893" size="354,56" zPosition="1" font="Regular; 28" halign="center" valign="center" backgroundColor="FNCMainListColor" transparent="0" foregroundColor="FNCMainFontColor" />\n        <widget name="key_green" position="602,893" size="354,56" zPosition="1" font="Regular; 28" halign="center" valign="center" backgroundColor="FNCMainListColor" transparent="0" foregroundColor="FNCMainFontColor" />\n        <widget name="key_yellow" position="969,893" size="354,56" zPosition="1" font="Regular; 28" halign="center" valign="center" backgroundColor="FNCMainListColor" transparent="0" foregroundColor="FNCMainFontColor" />\n\n        <widget name="config" position="250,240" size="1260,224" scrollbarMode="showOnDemand" font="Regular; 28" itemHeight="48" selectionPixmap="Estuary/selections/selection.png" backgroundPixmap="Estuary/list/separator_48.png" transparent="1" scrollbarSliderForegroundColor="FNCMainFontColor" scrollbarSliderBorderColor="FNCMainListColor" scrollbarSliderPicture="Estuary/list/bar_01.png" />\n\n        <widget name="tempc"  position="250,520"  size="580,50" font="Regular; 28" valign="center" halign="left" />\n        <widget name="voltc"  position="250,580"  size="580,50" font="Regular; 28" valign="center" halign="left" />\n        <widget name="frqc"   position="250,640"  size="580,50" font="Regular; 28" valign="center" halign="left" />\n\n        <eLabel name="" position="1542,372" size="145,50" font="Regular; 28" valign="center" halign="center" text="OK" />\n</screen>'
        Screen.__init__(self, session)
        self.onClose.append(self.abort)
        self.onChangedEntry = []
        self.list = []
        ConfigListScreen.__init__(self, self.list, session=self.session, on_change=self.changedEntry)
        self.createSetup()
        self['key_red'] = Button(_('Cancel'))
        self['key_green'] = Button(_('Save'))
        self['key_yellow'] = Button(_('Test'))
        self['setupActions'] = ActionMap(['SetupActions', 'ColorActions'], {'save': self.save,
           'cancel': self.cancel,
           'ok': self.save,
           'yellow': self.Test}, -2)

    def createSetup(self):
        print('[BrcmFRQ] createSetup initializing')
        self.editListEntry = None
        self.list = []
        self.list.append(getConfigListEntry(_('Set MAX CPU frequency'), config.plugins.brcm.maxfrq))
        self.list.append(getConfigListEntry(_('Set MIN CPU frequency'), config.plugins.brcm.minfrq))
        self.list.append(getConfigListEntry(_('Set Scaling governor'), config.plugins.brcm.governor))
        self['config'].list = self.list
        self['config'].l.setList(self.list)
        self['tempc'] = Label()
        self['voltc'] = Label()
        self['frqc'] = Label()
        self.timer = eTimer()
        if self.getcurrentData not in self.timer.callback:
            print('[BrcmFRQ] createSetup in Timer')
            self.timer.callback.append(self.getcurrentData)
            self.timer.start(2000, True)
        return

    def getcurrentData(self):
        self.temp = 'N/A'
        self.voltage = 'N/A'
        self.cfrq = 'N/A'
        if platform == 'edision4k':
            try:
                f = open('/proc/stb/fp/temp_sensor_avs', 'r')
                self.temp = f.read()
                self.temp = self.temp.strip()
                f.close()
                f = open('/sys/devices/system/cpu/cpufreq/policy0/brcm_avs_voltage', 'r')
                self.voltage = f.read()
                self.voltage = self.voltage.strip()
                f.close()
                f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r')
                self.cfrq = f.read()
                self.cfrq = self.cfrq.strip()
                f.close()
            except:
                pass

            try:
                self.voltage = str(int(self.voltage, 16))
                self.cfrq = str(int(self.cfrq.strip()) / 1000)
            except:
                pass

        self['tempc'].setText(_('Current Temperature (SoC):  ' + self.temp + ' C'))
        self['voltc'].setText(_('Current CPU Voltage:  ' + self.voltage + ' mV'))
        self['frqc'].setText(_('Current CPU Frequency:  ' + self.cfrq + ' MHz'))
        self.timer.start(1000, True)

    def changedEntry(self):
        for x in self.onChangedEntry:
            x()

        self.newConfig()

    def newConfig(self):
        print(self['config'].getCurrent()[0])
        if self['config'].getCurrent()[0] == _('Start Boot Frequency'):
            self.createSetup()

    def abort(self):
        self.timer.stop()
        if self.getcurrentData in self.timer.callback:
            self.timer.callback.remove(self.getcurrentData)
        print('[BrcmFRQ] aborting')

    def save(self):
        for x in self['config'].list:
            x[1].save()

        configfile.save()
        initBooster()
        self.close()

    def cancel(self):
        initBooster()
        for x in self['config'].list:
            x[1].cancel()

        self.close()

    def Test(self):
        initBooster()


class U5_Booster:

    def __init__(self, session):
        print('[BrcmFRQ] U5_Booster initializing')
        self.session = session
        self.service = None
        self.onClose = []
        initBooster()
        return

    def shutdown(self):
        self.abort()

    def abort(self):
        self.timer.stop()
        if self.getcurrentData in self.timer.callback:
            self.timer.callback.remove(self.getcurrentData)
        print('[BrcmFRQ] U5_Booster aborting')

    config.misc.standbyCounter.addNotifier(standbyCounterChanged, initial_call=False)


def main(menuid):
    if menuid != 'system':
        return []
    else:
        return [
         (
          _('CPU Control'), startBooster, 'CPU Control', None)]


def startBooster(session, **kwargs):
    session.open(BrcmFRQ)


wbooster = None
gReason = -1
mySession = None


def dinobotbooster():
    global gReason
    global mySession
    global wbooster
    if gReason == 0 and mySession != None and wbooster == None:
        print('[BrcmFRQ] Dinobooster Starting !!')
        wbooster = U5_Booster(mySession)
    elif gReason == 1 and wbooster != None:
        print('[BrcmFRQ] Dinobooster Stopping !!')
        wbooster = None
    return


def sessionstart(reason, **kwargs):
    global gReason
    global mySession
    print('[BrcmFRQ] sessionstart')
    if 'session' in kwargs:
        mySession = kwargs['session']
    else:
        gReason = reason
    dinobotbooster()


def Plugins(**kwargs):
    return [
     PluginDescriptor(where=[PluginDescriptor.WHERE_AUTOSTART, PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionstart),
     PluginDescriptor(name='BRCM FRQ Setup', description='Set speed settings for Broadcom CPUs', where=PluginDescriptor.WHERE_MENU, fnc=main)]
