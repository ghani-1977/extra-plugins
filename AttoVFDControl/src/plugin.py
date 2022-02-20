
from . import _
from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.Console import Console
from Components.Button import Button
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigList
from Components.config import config, configfile, ConfigSubsection, getConfigListEntry, ConfigSelection
from Components.ConfigList import ConfigListScreen
from enigma import eServiceCenter, eTimer, eActionMap
from Screens.InfoBar import InfoBar
from time import localtime, time
import Screens.Standby

config.plugins.VFD_atto = ConfigSubsection()
config.plugins.VFD_atto.showClock = ConfigSelection(default='True_Switch', choices=[('False', _('Channelnumber in Standby off')),
 ('True', _('Channelnumber in Standby Clock')),
 ('True_Switch', _('Channelnumber/Clock in Standby Clock')),
 ('True_All', _('Clock always')),
 ('Off', _('Always off'))])
config.plugins.VFD_atto.timeMode = ConfigSelection(default='24h', choices=['12h', '24h'])


def vfd_write(text):
    try:
        open("/dev/player/panel", "w").write("%s\n" % text)
    except:
        pass


class Channelnumber:
    def __init__(self, session):
        self.session = session
        self.updatetime = 10000
        self.blink = False
        self.channelnrdelay = 15
        self.begin = int(time())
        self.endkeypress = True
        eActionMap.getInstance().bindAction('', -2147483647, self.keyPressed)
        self.zaPrik = eTimer()
        self.zaPrik.timeout.get().append(self.vrime)
        self.zaPrik.start(1000, 1)
        self.onClose = []
        self.__event_tracker = False

    def __eventInfoChanged(self):
        if config.plugins.VFD_atto.showClock.value == 'Off' or config.plugins.VFD_atto.showClock.value == 'True_All':
            return
        else:
            service = self.session.nav.getCurrentService()
            info = service and service.info()
            if info is None:
                chnr = '----'
            else:
                chnr = self.getChannelNumber()
            info = None
            service = None
            if chnr == '----':
                vfd_write(chnr)
            else:
                Channelnr = '%04d' % int(chnr)
                vfd_write(Channelnr)
            return
            return

    def getChannelNumber(self):
        if InfoBar.instance is None:
            chnr = '----'
            return chnr
        else:
            MYCHANSEL = InfoBar.instance.servicelist
            markersOffset = 0
            myRoot = MYCHANSEL.getRoot()
            mySrv = MYCHANSEL.servicelist.getCurrent()
            chx = MYCHANSEL.servicelist.l.lookupService(mySrv)
            if not MYCHANSEL.inBouquet():
                pass
            else:
                serviceHandler = eServiceCenter.getInstance()
                mySSS = serviceHandler.list(myRoot)
                SRVList = mySSS and mySSS.getContent('SN', True)
                for i in range(len(SRVList)):
                    if chx == i:
                        break
                    testlinet = SRVList[i]
                    testline = testlinet[0].split(':')
                    if testline[1] == '64':
                        markersOffset = markersOffset + 1

            chx = chx - markersOffset + 1
            rx = MYCHANSEL.getBouquetNumOffset(myRoot)
            chnr = str(chx + rx)
            return chnr
            return

    def show(self):
        if config.plugins.VFD_atto.showClock.value == 'True' or config.plugins.VFD_atto.showClock.value == 'True_All' or config.plugins.VFD_atto.showClock.value == 'True_Switch':
            clock = str(localtime()[3])
            clock1 = str(localtime()[4])
            if config.plugins.VFD_atto.timeMode.value != '24h':
                if int(clock) > 12:
                    clock = str(int(clock) - 12)

            vfd_write('%02d:%02d' % (int(clock), int(clock1)))
        else:
            vfd_write('....')

    def vrime(self):
        if (config.plugins.VFD_atto.showClock.value == 'True' or config.plugins.VFD_atto.showClock.value == 'False' or config.plugins.VFD_atto.showClock.value == 'True_Switch') and not Screens.Standby.inStandby:
            if config.plugins.VFD_atto.showClock.value == 'True_Switch':
                if time() >= self.begin:
                    self.endkeypress = False
                if self.endkeypress:
                    self.__eventInfoChanged()
                else:
                    self.show()
            else:
                self.__eventInfoChanged()
        if config.plugins.VFD_atto.showClock.value == 'Off':
            vfd_write('....')
            self.zaPrik.start(self.updatetime, 1)
            return
        self.zaPrik.start(1000, 1)
        if Screens.Standby.inStandby or config.plugins.VFD_atto.showClock.value == 'True_All':
            self.show()

    def keyPressed(self, key, tag):
        self.begin = time() + int(self.channelnrdelay)
        self.endkeypress = True


ChannelnumberInstance = None


def leaveStandby():
    print('[VFD-ATTO] Leave Standby')
    if config.plugins.VFD_atto.showClock.value == 'Off':
        vfd_write('....')


def standbyCounterChanged(configElement):
    print('[VFD-ATTO] In Standby')
    from Screens.Standby import inStandby
    inStandby.onClose.append(leaveStandby)
    if config.plugins.VFD_atto.showClock.value == 'Off':
        vfd_write('....')


def initVFD():
    print('[VFD-ATTO] initVFD')
    if config.plugins.VFD_atto.showClock.value == 'Off':
        vfd_write('....')


class VFD_ATTOSetup(ConfigListScreen, Screen):
    skin = '<screen position="100,100" size="500,210" title="LED Display Setup" >\n\t\t\t\t<widget name="config" position="20,15" size="460,150" scrollbarMode="showOnDemand" />\n\t\t\t\t<ePixmap position="40,165" size="140,40" pixmap="skin_default/buttons/green.png" alphatest="on" />\n\t\t\t\t<ePixmap position="180,165" size="140,40" pixmap="skin_default/buttons/red.png" alphatest="on" />\n\t\t\t\t<widget name="key_green" position="40,165" size="140,40" font="Regular;20" backgroundColor="#1f771f" zPosition="2" transparent="1" shadowColor="black" shadowOffset="-1,-1" />\n\t\t\t\t<widget name="key_red" position="180,165" size="140,40" font="Regular;20" backgroundColor="#9f1313" zPosition="2" transparent="1" shadowColor="black" shadowOffset="-1,-1" />\n\t\t\t</screen>'

    def __init__(self, session, args=None):
        Screen.__init__(self, session)
        Screen.setTitle(self, _('7-LED Display Setup'))
        self.skinName = ['Setup']
        self.onClose.append(self.abort)
        self.onChangedEntry = []
        self.list = []
        ConfigListScreen.__init__(self, self.list, session=self.session, on_change=self.changedEntry)
        self.createSetup()
        self.Console = Console()
        self['key_red'] = Button(_('Cancel'))
        self['key_green'] = Button(_('Save'))
        self['setupActions'] = ActionMap(['SetupActions', 'ColorActions'], {'save': self.save,
         'cancel': self.cancel,
         'ok': self.save}, -2)

    def createSetup(self):
        self.editListEntry = None
        self.list = []
        self.list.append(getConfigListEntry(_('Show on display'), config.plugins.VFD_atto.showClock))
        if config.plugins.VFD_atto.showClock.value != 'Off':
            self.list.append(getConfigListEntry(_('Time mode'), config.plugins.VFD_atto.timeMode))
        self['config'].list = self.list
        self['config'].l.setList(self.list)
        return

    def changedEntry(self):
        for x in self.onChangedEntry:
            x()

        self.newConfig()

    def newConfig(self):
        print(self['config'].getCurrent()[0])
        if self['config'].getCurrent()[0] == _('Show on display'):
            self.createSetup()

    def abort(self):
        print('aborting')

    def save(self):
        for x in self['config'].list:
            x[1].save()

        configfile.save()
        initVFD()
        self.close()

    def cancel(self):
        initVFD()
        for x in self['config'].list:
            x[1].cancel()

        self.close()


class VFD_ATTO:

    def __init__(self, session):
        global ChannelnumberInstance
        print('[VFD-ATTO] initializing')
        self.session = session
        self.service = None
        self.onClose = []
        self.Console = Console()
        initVFD()
        if ChannelnumberInstance is None:
            ChannelnumberInstance = Channelnumber(session)
        return

    def shutdown(self):
        self.abort()

    def abort(self):
        print('[VFD-ATTO] aborting')
        config.misc.standbyCounter.addNotifier(standbyCounterChanged, initial_call=False)


def main(menuid):
    if menuid != 'system':
        return []
    else:
        return [(_('LED Display Setup'),
          startVFD,
          'VFD_ATTO',
          None)]
        return None


def startVFD(session, **kwargs):
    session.open(VFD_ATTOSetup)


attoVfd = None
gReason = -1
mySession = None


def controlattoVfd():
    global gReason
    global mySession
    global attoVfd
    if gReason == 0 and mySession != None and attoVfd == None:
        print('[VFD-ATTO] Starting !!')
        attoVfd = VFD_ATTO(mySession)
    elif gReason == 1 and attoVfd != None:
        print('[VFD-ATTO] Stopping !!')
        attoVfd = None
    return


def sessionstart(reason, **kwargs):
    global mySession
    global gReason
    print('[VFD-ATTO] sessionstart')
    if 'session' in kwargs:
        mySession = kwargs['session']
    else:
        gReason = reason
    controlattoVfd()


def Plugins(**kwargs):
    return [PluginDescriptor(where=[PluginDescriptor.WHERE_AUTOSTART, PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionstart), PluginDescriptor(name='Atto LED Display Setup', description='Change VFD display settings', where=PluginDescriptor.WHERE_MENU, fnc=main)]
