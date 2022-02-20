#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from Screens.Screen import Screen
from Screens.Console import Console
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox
from Screens.VirtualKeyBoard import VirtualKeyBoard
from Components.Button import Button
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Label import Label
from Components.ProgressBar import ProgressBar
from Components.Pixmap import Pixmap
from Components.config import *
from Components.ConfigList import ConfigListScreen
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import fileExists, pathExists
import os
from skin import parseColor
from Plugins.Plugin import PluginDescriptor
from Components.Console import Console
from Components.SystemInfo import BoxInfo

visionversion = BoxInfo.getItem("imgversion")
visionrevision = BoxInfo.getItem("imgrevision")
brand = BoxInfo.getItem("brand")
model = BoxInfo.getItem("model")
distro = BoxInfo.getItem("distro")

SH4MultiBootInstallation_Skin = '\n\t\t<screen name="SH4MultiBootInstallation" position="center,center" size="902,380" title="SH4MultiBoot - Installation" >\n\t\t      <widget name="label1" position="10,10" size="840,30" zPosition="1" halign="center" font="Regular;25" backgroundColor="#9f1313" transparent="1"/>\n\t\t      <widget name="label2" position="10,80" size="840,290" zPosition="1" halign="center" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t      <widget name="config" position="10,160" size="840,200" scrollbarMode="showOnDemand" transparent="1"/>\n\t\t      <ePixmap pixmap="skin_default/buttons/red.png" position="10,290" size="140,40" alphatest="on" />\n\t\t      <ePixmap pixmap="skin_default/buttons/green.png" position="150,290" size="140,40" alphatest="on" />\n\t\t      <ePixmap pixmap="skin_default/buttons/blue.png" position="385,290" size="140,40" alphatest="on" />\n\t\t      <widget name="key_red" position="10,290" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t      <widget name="key_green" position="160,290" zPosition="1" size="200,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t      <widget name="key_blue" position="416,290" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />\n\t\t</screen>'

SH4MultiBootImageChoose_Skin = '\n\t\t<screen name="SH4MultiBootImageChoose" position="center,center" size="902,380" title="SH4MultiBoot - Menu" >\n\t\t\t<widget name="label2" position="145,10" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label3" position="145,35" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label4" position="145,60" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label5" position="145,85" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label6" position="420,10" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label7" position="420,35" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label8" position="420,60" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label9" position="420,85" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label10" position="145,110" size="600,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label11" position="420,110" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label1" position="25,145" size="840,22" zPosition="1" halign="center" font="Regular;18" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="device_icon" position="25,20" size="80,80" alphatest="on" />\n\t\t\t<widget name="free_space_progressbar" position="265,42" size="500,13" borderWidth="1" zPosition="3" />\n\t\t\t<widget name="config" position="25,180" size="840,150" scrollbarMode="showOnDemand"/>\n\t\t\t<ePixmap pixmap="skin_default/buttons/red.png" position="10,340" size="150,40" alphatest="on" />\n\t\t\t<ePixmap pixmap="skin_default/buttons/green.png" position="260,340" size="150,40" alphatest="on" />\n\t\t\t<ePixmap pixmap="skin_default/buttons/yellow.png" position="520,340" size="150,40" alphatest="on" />\n\t\t\t<ePixmap pixmap="skin_default/buttons/blue.png" position="750,340" size="150,40" alphatest="on" />\n\t\t\t<widget name="key_red" position="5,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t\t<widget name="key_green" position="255,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t\t<widget name="key_yellow" position="515,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />\n\t\t\t<widget name="key_blue" position="745,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />\n\t\t</screen>'

SH4MultiBootImageInstall_Skin = '\n\t\t    <screen name="SH4MultiBootImageInstall" position="center,center" size="770,340" title="SH4MultiBoot - Image Installation" >\n\t\t\t      <widget name="config" position="10,10" size="750,220" scrollbarMode="showOnDemand" transparent="1"/>\n\t\t\t      <ePixmap pixmap="skin_default/buttons/red.png" position="10,290" size="140,40" alphatest="on" />\n\t\t\t      <ePixmap pixmap="skin_default/buttons/green.png" position="150,290" size="140,40" alphatest="on" />\n\t\t\t      <ePixmap pixmap="skin_default/buttons/yellow.png" position="290,290" size="140,40" alphatest="on" />\n\t\t\t      <widget name="HelpWindow" position="330,310" zPosition="5" size="1,1" transparent="1" alphatest="on" />      \n\t\t\t      <widget name="key_red" position="10,290" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t\t      <widget name="key_green" position="150,290" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t\t      <widget name="key_yellow" position="290,290" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />\n\t\t    </screen>'


def Freespace(dev):
    statdev = os.statvfs(dev)
    space = statdev.f_bavail * statdev.f_frsize / 1024
    print('[SH4MultiBoot] Free space on %s = %i kilobytes' % (dev, space))
    return space


class SH4MultiBootInstallation(Screen):

    def __init__(self, session):
        self.skin = SH4MultiBootInstallation_Skin
        Screen.__init__(self, session)
        self.list = []
        self['config'] = MenuList(self.list)
        self['key_red'] = Label(_('Install'))
        self['key_green'] = Label(_('Mount Manager'))
        self['key_blue'] = Label(_('Devices Panel'))
        self['label1'] = Label(_('Welcome to SH4MultiBoot %s-%s plugin installation for %s %s') % (visionversion, visionrevision, brand, model))
        self['label2'] = Label(_('Here is the list of mounted devices on your receiver.\n\nPlease choose a device where you would like to install SH4MultiBoot:'))
        self['actions'] = ActionMap(['WizardActions', 'ColorActions'], {'red': self.install,
         'green': self.mountmanager,
         'blue': self.devpanel,
         'back': self.close})
        self.updateList()

    def updateList(self):
        myusb, myhdd = ('', '')
        myoptions = []
        if fileExists('/proc/mounts'):
            fileExists('/proc/mounts')
            f = open('/proc/mounts', 'r')
            for line in f.readlines():
                if line.find('/media/usb') != -1:
                    myusb = '/media/usb/'
                    continue
                if line.find('/hdd') != -1:
                    myhdd = '/media/hdd/'
                    continue

            f.close()
        else:
            self['label2'].setText(_('Sorry it seems there are not Linux formatted devices mounted on your receiver. To install SH4MultiBoot you need a Linux formatted part1 device. Click on the blue button to open Devices panel'))
            fileExists('/proc/mounts')
        if myusb:
            self.list.append(myusb)
        else:
            myusb
        if myhdd:
            myhdd
            self.list.append(myhdd)
        else:
            myhdd
        self['config'].setList(self.list)

    def mountmanager(self):
        try:
            from Plugins.SystemPlugins.Vision.MountManager import VISIONDevicesPanel
            self.session.open(VISIONDevicesPanel)
        except:
            self.session.open(MessageBox, _('You need to install vision-core plugin first.'), MessageBox.TYPE_INFO)

    def devpanel(self):
        try:
            from Screens.HarddiskSetup import HarddiskSelection
            self.session.open(HarddiskSelection)
        except:
            self.session.open(MessageBox, _('You are not running a proper open source image. You must mount devices yourself.'), MessageBox.TYPE_INFO)

    def myclose(self):
        self.close()

    def myclose2(self, message):
        self.session.open(MessageBox, message, MessageBox.TYPE_INFO)
        Console().ePopen('reboot -p')
        self.close()

    def checkReadWriteDir(self, configele):
        import os.path
        import Components.Harddisk
        supported_filesystems = frozenset(('ext4', 'ext3', 'ext2', 'nfs'))
        candidates = []
        mounts = Components.Harddisk.getProcMounts()
        for partition in Components.Harddisk.harddiskmanager.getMountedPartitions(False, mounts):
            if partition.filesystem(mounts) in supported_filesystems:
                candidates.append((partition.description, partition.mountpoint))

        if candidates:
            locations = []
            for validdevice in candidates:
                locations.append(validdevice[1])

            if Components.Harddisk.findMountPoint(os.path.realpath(configele)) + '/' in locations or Components.Harddisk.findMountPoint(os.path.realpath(configele)) in locations:
                if fileExists(configele, 'w'):
                    return True
                else:
                    dir = configele
                    self.session.open(MessageBox, _('The directory %s is not writable.\nMake sure you select a writable directory instead.') % dir, type=MessageBox.TYPE_ERROR)
                    return False
            else:
                dir = configele
                self.session.open(MessageBox, _('The directory %s is not a EXT2, EXT3, EXT4 or NFS partition.\nMake sure you select a valid partition type.') % dir, type=MessageBox.TYPE_ERROR)
                return False
        else:
            dir = configele
            self.session.open(MessageBox, _('The directory %s is not a EXT2, EXT3, EXT4 or NFS partition.\nMake sure you select a valid partition type.') % dir, type=MessageBox.TYPE_ERROR)
            return False

    def install(self):
        check = False
        if fileExists('/proc/mounts'):
            fileExists('/proc/mounts')
            f = open('/proc/mounts', 'r')
            for line in f.readlines():
                if line.find('/media/usb') != -1:
                    check = True
                    continue
                if line.find('/hdd') != -1:
                    check = True
                    continue

            f.close()
        else:
            fileExists('/proc/mounts')
        if check == False:
            self.session.open(MessageBox, _('Sorry, there is not any connected devices on your receiver.\nPlease connect HDD or USB to install SH4MultiBoot!'), MessageBox.TYPE_INFO)
        else:
            fileExists('/boot/dummy')
            self.mysel = self['config'].getCurrent()
            if self.checkReadWriteDir(self.mysel):
                message = _('Do You really want to install SH4MultiBoot on:\n ') + self.mysel + '?\nYour receiver will reboot after choice '
                ybox = self.session.openWithCallback(self.install2, MessageBox, message, MessageBox.TYPE_YESNO)
                ybox.setTitle(_('Install Confirmation'))
            else:
                self.close()

    def install2(self, yesno):
        if yesno:
            cmd2 = 'mkdir -p /media/sh4multiboot;mount ' + self.mysel + ' /media/sh4multiboot'
            Console().ePopen(cmd2)
            if fileExists('/proc/mounts'):
                fileExists('/proc/mounts')
                f = open('/proc/mounts', 'r')
                for line in f.readlines():
                    if line.find(self.mysel):
                        mntdev = line.split(' ')[0]
                f.close()
                mntid = Console().ePopen('blkid -s UUID -o value %s>/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/bin/install' % mntdev)

            cmd = 'mkdir -p ' + self.mysel + 'SH4MultiBootI;mkdir -p ' + self.mysel + 'SH4MultiBootUpload'
            Console().ePopen(cmd)
            Console().ePopen('cp -f /usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/bin/sh4multiinit /sbin/sh4multiinit')
            Console().ePopen('chmod 777 /sbin/sh4multiinit;chmod 777 /sbin/init;ln -sfn /sbin/sh4multiinit /sbin/init')
            Console().ePopen('mv -f /etc/init.d/volatile-media.sh /etc/init.d/volatile-media.sh.back')
            open('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot', 'w').write('Flash')
            open('/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/.sh4multiboot_location', 'w').write(self.mysel)
            Console().ePopen('cp -f /usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/.sh4multiboot_location /etc/sh4multi/')
            image = distro
            if fileExists('/etc/image-version'):
                if 'build' not in image:
                    f = open('/etc/image-version', 'r')
                    for line in f.readlines():
                        if 'build=' in line:
                            image = image + ' build ' + line[6:-1]
                            open('/media/sh4multiboot/SH4MultiBootI/.Flash', 'w').write(image)
                            break

                    f.close()
            self.myclose2(_('SH4MultiBoot has been installed succesfully!'))
        else:
            self.session.open(MessageBox, _('Installation aborted !'), MessageBox.TYPE_INFO)


class SH4MultiBootImageChoose(Screen):

    def __init__(self, session):
        self.skin = SH4MultiBootImageChoose_Skin
        Screen.__init__(self, session)
        self.list = []
        self.setTitle('SH4MultiBoot %s-%s running on %s %s' % (visionversion, visionrevision, brand, model))
        self['device_icon'] = Pixmap()
        self['free_space_progressbar'] = ProgressBar()
        self['linea'] = ProgressBar()
        self['config'] = MenuList(self.list)
        self['key_red'] = Label(_('Boot Image'))
        self['key_green'] = Label(_('Install Image'))
        self['key_yellow'] = Label(_('Remove Image '))
        self['key_blue'] = Label(_('Uninstall'))
        self['label2'] = Label(_('SH4MultiBoot is running from:'))
        self['label3'] = Label(_('Used:'))
        self['label4'] = Label(_('Available:'))
        self['label5'] = Label(_('SH4MultiBoot is running image:'))
        self['label6'] = Label('')
        self['label7'] = Label('')
        self['label8'] = Label('')
        self['label9'] = Label('')
        self['label10'] = Label(_('Number of installed images in SH4MultiBoot (100 allowed):'))
        self['label11'] = Label('')
        self['label1'] = Label(_('Here is the list of installed images on your receiver. Please choose an image to boot.'))
        self['actions'] = ActionMap(['WizardActions', 'ColorActions'], {'red': self.boot,
         'green': self.install,
         'yellow': self.remove,
         'blue': self.advanced,
         'back': self.close})
        self.onShow.append(self.updateList)

    def updateList(self):
        self.list = []
        try:
            pluginpath = '/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot'
            mypath = open(pluginpath + '/.sh4multiboot_location', 'r').readline().strip()
        except:
            mypath = '/media/hdd'

        icon = 'dev_usb.png'
        if 'hdd' in mypath:
            icon = 'dev_hdd.png'
        icon = pluginpath + '/images/' + icon
        png = LoadPixmap(icon)
        self['device_icon'].instance.setPixmap(png)
        device = '/media/sh4multiboot'
        dev_free = dev_free_space = def_free_space_percent = ''
        rc = Console().ePopen('df > /tmp/ninfo.tmp')
        if fileExists('/tmp/ninfo.tmp'):
            f = open('/tmp/ninfo.tmp', 'r')
            for line in f.readlines():
                line = line.replace('part1', ' ')
                parts = line.strip().split()
                totsp = len(parts) - 1
                if parts[totsp] == device:
                    if totsp == 5:
                        dev_free = parts[1]
                        dev_free_space = parts[3]
                        def_free_space_percent = parts[4]
                    else:
                        dev_free = 'N/A   '
                        dev_free_space = parts[2]
                        def_free_space_percent = parts[3]
                    break

            f.close()
            os.remove('/tmp/ninfo.tmp')
        self.availablespace = dev_free_space[0:-3]
        perc = int(def_free_space_percent[:-1])
        self['free_space_progressbar'].setValue(perc)
        green = '#00389416'
        red = '#00ff2525'
        yellow = '#00ffe875'
        orange = '#00ff7f50'
        if perc < 30:
            color = green
        elif perc < 60:
            color = yellow
        elif perc < 80:
            color = orange
        else:
            color = red
        self['label6'].instance.setForegroundColor(parseColor(color))
        self['label7'].instance.setForegroundColor(parseColor(color))
        self['label8'].instance.setForegroundColor(parseColor(color))
        self['label9'].instance.setForegroundColor(parseColor(color))
        self['label11'].instance.setForegroundColor(parseColor(color))
        self['free_space_progressbar'].instance.setForegroundColor(parseColor(color))
        try:
            mypath2 = open('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot', 'r').readline().strip()
        except:
            mypath2 = 'Flash'

        if mypath2 == 'Flash':
            image = distro
            if fileExists('/etc/image-version'):
                if 'build' not in image:
                    f = open('/etc/image-version', 'r')
                    for line in f.readlines():
                        if 'build=' in line:
                            image = image + ' build ' + line[6:-1]
                            open('/media/sh4multiboot/SH4MultiBootI/.Flash', 'w').write(image)
                            break

                    f.close()
        elif fileExists('/media/sh4multiboot/SH4MultiBootI/.Flash'):
            image = open('/media/sh4multiboot/SH4MultiBootI/.Flash', 'r').readline().strip()
        image = ' [' + image + ']'
        self.list.append('Flash' + image)
        self['label6'].setText(mypath)
        self['label7'].setText(def_free_space_percent)
        self['label8'].setText(dev_free_space[0:-3] + ' MB')
        self['label9'].setText(mypath2)
        mypath = '/media/sh4multiboot/SH4MultiBootI/'
        myimages = os.listdir(mypath)
        for fil in myimages:
            if os.path.isdir(os.path.join(mypath, fil)):
                self.list.append(fil)

        self['label11'].setText(str(len(self.list) - 1))
        self['config'].setList(self.list)

    def myclose(self):
        self.close()

    def myclose2(self, message):
        self.session.open(MessageBox, message, MessageBox.TYPE_INFO)
        self.close()

    def boot(self):
        self.mysel = self['config'].getCurrent()
        if self.mysel:
            open('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot', 'w').write(self.mysel)
            Console().ePopen('rm -f /tmp/.sh4multireboot')
            message = _('Are you sure you want to boot:\n') + self.mysel + ' now?'
            ybox = self.session.openWithCallback(self.boot2, MessageBox, message, MessageBox.TYPE_YESNO)
            ybox.setTitle(_('Boot Confirmation'))
        else:
            self.mysel

    def boot2(self, yesno):
        if yesno:
            Console().ePopen('touch /tmp/.sh4multireboot')
            Console().ePopen('reboot -p')
        else:
            Console().ePopen('touch /tmp/.sh4multireboot')
            self.session.open(MessageBox, _('Image will be booted after the next receiver reboot.'), MessageBox.TYPE_INFO)

    def remove(self):
        self.mysel = self['config'].getCurrent()
        if self.mysel:
            mypath = open('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot', 'r').readline().strip()
            try:
                if mypath == self.mysel:
                    self.session.open(MessageBox, _('Sorry you cannot delete the image currently booted from.'), MessageBox.TYPE_INFO, 4)
                if self.mysel.startswith('Flash'):
                    self.session.open(MessageBox, _('Sorry you cannot delete Flash image'), MessageBox.TYPE_INFO, 4)
                else:
                    open('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot', 'w').write('Flash')
                    message = _('Are you sure you want to delete:\n ') + self.mysel + ' now?'
                    ybox = self.session.openWithCallback(self.remove2, MessageBox, message, MessageBox.TYPE_YESNO)
                    ybox.setTitle(_('Delete Confirmation'))
            except:
                print('[SH4MultiBoot] No image to remove')

        else:
            self.mysel

    def up(self):
        self.list = []
        self['config'].setList(self.list)
        self.updateList()

    def up2(self):
        try:
            self.list = []
            self['config'].setList(self.list)
            self.updateList()
        except:
            print(' ')

    def remove2(self, yesno):
        if yesno:
            cmd = "echo -e '\n\nSH4MultiBoot deleting image ... '"
            cmd1 = 'rm -rf /media/sh4multiboot/SH4MultiBootI/' + self.mysel
            self.session.openWithCallback(self.up, Console, _('SH4MultiBoot: Deleting image'), [cmd, cmd1])
        else:
            self.session.open(MessageBox, _('Removing canceled!'), MessageBox.TYPE_INFO)

    def installMedia(self):
        images = False
        myimages = os.listdir('/media/sh4multiboot/SH4MultiBootUpload')
        print(myimages)
        for fil in myimages:
            if fil.endswith('.zip'):
                images = True
                break
            else:
                images = False

        if images == True:
            self.session.openWithCallback(self.up2, SH4MultiBootImageInstall)
        else:
            mess = _('The /media/sh4multiboot/SH4MultiBootUpload directory is empty!\n\nPlease upload one image file first.\nZip format for example.\n\n')
            self.session.open(MessageBox, mess, MessageBox.TYPE_INFO)

    def install(self):
        count = 0
        for fn in os.listdir('/media/sh4multiboot/SH4MultiBootI'):
            dirfile = '/media/sh4multiboot/SH4MultiBootI/' + fn
            if os.path.isdir(dirfile):
                count = count + 1

        if count > 100:
            myerror = _('Sorry you can install a max of 100 images.')
            self.session.open(MessageBox, myerror, MessageBox.TYPE_INFO)
        else:
            menulist = []
            menulist.append((_('Install from /media/sh4multiboot/SH4MultiBootUpload'), 'media'))
            menulist.append((_('Install from internet'), 'internet'))
            self.session.openWithCallback(self.menuCallback, ChoiceBox, title='Choose they way for installation', list=menulist)

    def menuCallback(self, choice):
        self.show()
        if choice is None:
            return
        else:
            if choice[1] == 'internet':
                from Plugins.Extensions.SH4MultiBoot.download_images import SH4MultiChooseOnLineImage
                self.session.open(SH4MultiChooseOnLineImage)
            if choice[1] == 'media':
                self.installMedia()
            return

    def advanced(self):
        menulist = []
        menulist.append((_('Remove SH4MultiBoot'), 'rmsh4multiboot'))
        menulist.append((_('Remove all installed images'), 'rmallimg'))
        self.session.openWithCallback(self.menuAdvancedCallback, ChoiceBox, title=_('What would you like to do?'), list=menulist)

    def menuAdvancedCallback(self, choice):
        self.show()
        if choice is None:
            return
        else:
            if choice[1] == 'rmsh4multiboot':
                cmd0 = "echo -e '\n\nSH4MultiBoot preparing to remove ...'"
                cmd1 = 'rm -f /sbin/sh4multiinit'
                cmd1a = "echo -e '\n\nSH4MultiBoot removing boot manager ...'"
                cmd2 = 'rm -f /sbin/init'
                cmd3 = 'ln -sfn /sbin/init.sysvinit /sbin/init'
                cmd4 = 'chmod 777 /sbin/init'
                cmd4a = "echo -e '\n\nSH4MultiBoot restoring media mounts ...'"
                cmd5 = 'mv -f /etc/init.d/volatile-media.sh.back /etc/init.d/volatile-media.sh'
                cmd6 = 'rm -f /media/sh4multiboot/SH4MultiBootI/.sh4multiboot'
                cmd7 = 'rm -f /media/sh4multiboot/SH4MultiBootI/.Flash'
                cmd8 = 'rm -f /usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/.sh4multiboot_location'
                cmd8a = "echo -e '\n\nSH4MultiBoot remove completed.'"
                self.session.openWithCallback(self.close, Console, _('SH4MultiBoot is removing ...'), [cmd0,
                 cmd1,
                 cmd1a,
                 cmd2,
                 cmd3,
                 cmd4,
                 cmd4a,
                 cmd5,
                 cmd6,
                 cmd7,
                 cmd8,
                 cmd8a])
            if choice[1] == 'rmallimg':
                cmd = "echo -e '\n\nSH4MultiBoot deleting image ... '"
                cmd1 = 'rm -rf /media/sh4multiboot/SH4MultiBootI/*'
                self.session.openWithCallback(self.updateList, Console, _('SH4MultiBoot: Deleting all images'), [cmd, cmd1])
            return


class SH4MultiBootImageInstall(Screen, ConfigListScreen):

    def __init__(self, session):
        self.skin = SH4MultiBootImageInstall_Skin
        Screen.__init__(self, session)
        fn = 'NewImage'
        sourcelist = []
        for fn in os.listdir('/media/sh4multiboot/SH4MultiBootUpload'):
            if fn.find('.zip') != -1:
                fn = fn.replace('.zip', '')
                sourcelist.append((fn, fn))
                continue

        if len(sourcelist) == 0:
            sourcelist = [('None', 'None')]
        self.source = ConfigSelection(choices=sourcelist)
        self.target = ConfigText(fixed_size=False)
        self.settings = ConfigYesNo(default=False)
        self.zipdelete = ConfigYesNo(default=False)
        self.target.value = ''
        self.curselimage = ''
        try:
            if self.curselimage != self.source.value:
                self.target.value = self.source.value[:-13]
                self.curselimage = self.source.value
        except:
            pass

        self.createSetup()
        ConfigListScreen.__init__(self, self.list, session=session)
        self.source.addNotifier(self.typeChange)
        self['actions'] = ActionMap(['OkCancelActions',
         'ColorActions',
         'VirtualKeyboardActions'], {'cancel': self.cancel,
         'red': self.cancel,
         'green': self.imageInstall,
         'yellow': self.openKeyboard}, -2)
        self['key_green'] = Label(_('Install'))
        self['key_red'] = Label(_('Cancel'))
        self['key_yellow'] = Label(_('Keyboard'))
        self['HelpWindow'] = Pixmap()
        self['HelpWindow'].hide()

    def createSetup(self):
        self.list = []
        self.list.append(getConfigListEntry(_('Source image'), self.source))
        self.list.append(getConfigListEntry(_('Image name'), self.target))
        self.list.append(getConfigListEntry(_('Copy current settings to the new image?'), self.settings))
        self.list.append(getConfigListEntry(_('Delete downloaded zip file after install?'), self.zipdelete))

    def typeChange(self, value):
        self.createSetup()
        self['config'].l.setList(self.list)
        if self.curselimage != self.source.value:
            self.target.value = self.source.value[:-13]
            self.curselimage = self.source.value

    def openKeyboard(self):
        sel = self['config'].getCurrent()
        if sel:
            if sel == self.target:
                if self['config'].getCurrent()[1].help_window.instance is not None:
                    self['config'].getCurrent()[1].help_window.hide()
            self.vkvar = sel[0]
            if self.vkvar == _('Image name'):
                self.session.openWithCallback(self.VirtualKeyBoardCallback, VirtualKeyBoard, title=self['config'].getCurrent()[0], text=self['config'].getCurrent()[1].value)
        return

    def VirtualKeyBoardCallback(self, callback=None):
        if callback is not None and len(callback):
            self['config'].getCurrent()[1].setValue(callback)
            self['config'].invalidate(self['config'].getCurrent())
        return

    def imageInstall(self):
        filesys = BoxInfo.getItem("imagefs").replace(' ', '')
        if self.check_free_space():
            pluginpath = '/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot'
            myerror = ''
            source = self.source.value.replace(' ', '')
            target = self.target.value.replace(' ', '')
            for fn in os.listdir('/media/sh4multiboot/SH4MultiBootI'):
                if fn == target:
                    myerror = _('Sorry, an image with the name ') + target + _(' is already installed.\n Please try another name.')
                    continue

            if source == 'None':
                myerror = _('You have to select one image to install.\nPlease upload your zip file in this path: /media/sh4multiboot/SH4MultiBootUpload and select the image to install.')
            if target == '':
                myerror = _('You have to provide a name for the new image.')
            if target == 'Flash':
                myerror = _('Sorry Flash name is reserved. Choose another name for the new image.')
            if len(target) > 35:
                myerror = _('Sorry the name of the new image is too long.')
            if myerror:
                self.session.open(MessageBox, myerror, MessageBox.TYPE_INFO)
            else:
                message = "echo -e '\n\n"
                message += _('SH4MultiBoot will install the new image.\n\n')
                message += _('WARNING: Do not reboot your receiver and turn off the power!\n\n')
                message += _('The new image will be installed and auto booted in few minutes.\n\n')
                message += "'"
                if fileExists(pluginpath + '/ex_init.pyo'):
                    cmd1 = 'python ' + pluginpath + '/ex_init.pyo'
                else:
                    cmd1 = 'python ' + pluginpath + '/ex_init.py'
                cmd = '%s %s %s %s %s %s' % (cmd1,
                 source,
                 target.replace(' ', '.'),
                 str(self.settings.value),
                 filesys,
                 str(self.zipdelete.value))
                print('[SH4MultiBoot] Install command: ', cmd)
                self.session.open(Console, title=_('SH4MultiBoot: Install new image'), cmdlist=[message, cmd])

    def check_free_space(self):
        if Freespace('/media/sh4multiboot/SH4MultiBootUpload') < 500000:
            self.session.open(MessageBox, _('Not enough free space on /media/sh4multiboot/ !!\nYou need at least 500MB free space.\n\nExit plugin.'), type=MessageBox.TYPE_ERROR)
            return False
        return True

    def cancel(self):
        self.close()


def main(session, **kwargs):
    if not pathExists('/media/usb'):
        Console().ePopen('mkdir -p /media/usb')
    if pathExists('/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot'):
        try:
            mypath = open('/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/.sh4multiboot_location', 'r').readline().strip()
            if not pathExists('/media/sh4multiboot'):
                os.mkdir('/media/sh4multiboot')
            cmd = 'mount ' + mypath + ' /media/sh4multiboot'
            Console().ePopen(cmd)
            f = open('/proc/mounts', 'r')
            for line in f.readlines():
                if line.find('/media/sh4multiboot') != -1:
                    line = line[0:9]
                    break

            cmd = 'mount ' + line + ' ' + mypath
            Console().ePopen(cmd)
            cmd = 'mount ' + mypath + ' /media/sh4multiboot'
            Console().ePopen(cmd)
        except:
            pass

        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/.sh4multiboot_location'):
            if fileExists('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot'):
                session.open(SH4MultiBootImageChoose)
            else:
                session.open(SH4MultiBootInstallation)
        else:
            session.open(SH4MultiBootInstallation)
    else:
        session.open(MessageBox, _('Sorry: Wrong image in Flash found. You have to install the correct image in Flash'), MessageBox.TYPE_INFO, 3)


def menu(menuid, **kwargs):
    filename = '/etc/videomode2'
    if os.path.exists(filename):
        pass
    else:
        print("[SH4MultiBoot] Write to /etc/videomode2")
        open(filename, 'w').write("576i")
    if pathExists('/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot'):
        if menuid == 'mainmenu':
            return [(_('SH4MultiBoot'),
              main,
              'sh4multiboot',
              1)]
        return []
    else:
        return []


def Plugins(**kwargs):
    return [PluginDescriptor(name='SH4MultiBoot', description=_('E2 light MultiBoot for SH4'), icon='plugin.png', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
