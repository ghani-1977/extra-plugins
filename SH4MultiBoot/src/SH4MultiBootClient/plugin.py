#!/usr/bin/python
# -*- coding: utf-8 -*-

from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.Button import Button
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Label import Label
from Components.ProgressBar import ProgressBar
from Components.Pixmap import Pixmap
from Components.config import *
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import fileExists, pathExists
import os
from skin import parseColor
from Plugins.Plugin import PluginDescriptor
from Components.Console import Console

PLUGINVERSION = '7.6'

SH4MultiBootImageChoose_Skin = '\n\t\t<screen name="SH4MultiBootImageChooseClient" position="center,center" size="902,380" title="SH4MultiBoot - Client Menu" >\n\t\t\t<widget name="label2" position="145,10" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label3" position="145,35" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label4" position="145,60" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label5" position="145,85" size="440,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label6" position="420,10" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label7" position="420,35" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label8" position="420,60" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label9" position="420,85" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label10" position="145,110" size="600,30" zPosition="1" font="Regular;20" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="label11" position="420,110" size="440,30" zPosition="1" halign="right" font="Regular;20" backgroundColor="#9f1313" foregroundColor="#00389416" transparent="1"/>\n\t\t\t<widget name="label1" position="25,145" size="840,22" zPosition="1" halign="center" font="Regular;18" backgroundColor="#9f1313" transparent="1"/>\n\t\t\t<widget name="device_icon" position="25,20" size="80,80" alphatest="on" />\n\t\t\t<widget name="free_space_progressbar" position="265,42" size="500,13" borderWidth="1" zPosition="3" />\n\t\t\t<widget name="config" position="25,180" size="840,150" scrollbarMode="showOnDemand"/>\n\t\t\t<ePixmap pixmap="buttons/red.png" position="10,340" size="150,40" alphatest="on" />\n\t\t\t<ePixmap pixmap="buttons/green.png" position="260,340" size="150,40" alphatest="on" />\n\t\t\t<ePixmap pixmap="buttons/yellow.png" position="520,340" size="150,40" alphatest="on" />\n\t\t\t<ePixmap pixmap="buttons/blue.png" position="750,340" size="150,40" alphatest="on" />\n\t\t\t<widget name="key_red" position="5,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t\t<widget name="key_green" position="255,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />\n\t\t\t<widget name="key_yellow" position="515,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />\n\t\t\t<widget name="key_blue" position="745,340" zPosition="1" size="160,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />\n\t\t</screen>'


class SH4MultiBootImageChoose(Screen):

    def __init__(self, session):
        self.skin = SH4MultiBootImageChoose_Skin
        Screen.__init__(self, session)
        self.list = []
        self.setTitle('SH4MultiBoot %s Client' % PLUGINVERSION)
        self['device_icon'] = Pixmap()
        self['free_space_progressbar'] = ProgressBar()
        self['linea'] = ProgressBar()
        self['config'] = MenuList(self.list)
        self['key_red'] = Label(_('Boot Image'))
        self['label2'] = Label(_('SH4MultiBoot is running from:'))
        self['label3'] = Label(_('Used:'))
        self['label4'] = Label(_('Available:'))
        self['label7'] = Label('')
        self['label8'] = Label('')
        self['label10'] = Label(_('Number of installed images in SH4MultiBoot (100 allowed):'))
        self['label11'] = Label('')
        self['label1'] = Label(_('Here is the list of installed images on your receiver. Please choose an image to boot.'))
        self['actions'] = ActionMap(['WizardActions', 'ColorActions'], {'red': self.boot, 'back': self.close, })
        self.onShow.append(self.updateList)

    def updateList(self):
        self.list = []
        try:
            pluginpath = '/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBootClient'
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
        self['label7'].instance.setForegroundColor(parseColor(color))
        self['label8'].instance.setForegroundColor(parseColor(color))
        self['label11'].instance.setForegroundColor(parseColor(color))
        self['free_space_progressbar'].instance.setForegroundColor(parseColor(color))
        self.list.append('Flash')
        self['label7'].setText(def_free_space_percent)
        self['label8'].setText(dev_free_space[0:-3] + ' MB')
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
            message = _('Are you sure you want to boot:\n') + self.mysel + ' now ?'
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


def main(session, **kwargs):
    open('/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBootClient/.sh4multiboot_location', 'r').readline().strip()
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
    session.open(SH4MultiBootImageChoose)


def menu(menuid, **kwargs):
    filename = '/etc/videomode2'
    if os.path.exists(filename):
        pass
    else:
        print("[SH4MultiBoot] Write to /etc/videomode2")
        open(filename, 'w').write("576i")

    if menuid == 'mainmenu':
        return [(_('SH4MultiBoot Client'),
          main,
          'sh4multiboot',
          1)]
    return []


def Plugins(**kwargs):
    return [PluginDescriptor(name='SH4MultiBoot', description='SH4MultiBoot Client', where=PluginDescriptor.WHERE_MENU, fnc=menu), PluginDescriptor(name='SH4MultiBoot', description=_('SH4MultiBoot Client'), icon='plugin.png', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
