#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import shutil
from glob import glob


def SH4MultiBootMainEx(source, target, installsettings, filesys, zipdelete):
    sh4multihome = '/media/sh4multiboot'
    sh4multiroot = 'media/sh4multiboot'

    to = '/media/sh4multiboot/SH4MultiBootI/' + target
    cmd = 'rm -rf %s > /dev/null 2<&1' % to
    rc = os.system(cmd)
    to = '/media/sh4multiboot/SH4MultiBootI/' + target
    cmd = 'mkdir %s > /dev/null 2<&1' % to
    rc = os.system(cmd)
    to = '/media/sh4multiboot/SH4MultiBootI/' + target
    cmd = 'chmod -R 0777 %s' % to
    rc = os.system(cmd)
    print("[sh4multiboot] filesys:", filesys)
    if filesys == "jffs2":
        rc = SH4MultiBootExtractJFFS(source, target, zipdelete)
    cmd = 'mkdir -p %s/SH4MultiBootI/%s/media > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    cmd = 'rm -rf %s/SH4MultiBootI/%s/%s > /dev/null 2>&1' % (sh4multihome, target, sh4multiroot)
    rc = os.system(cmd)
    cmd = 'rmdir %s/SH4MultiBootI/%s/%s > /dev/null 2>&1' % (sh4multihome, target, sh4multiroot)
    rc = os.system(cmd)
    cmd = 'mkdir -p %s/SH4MultiBootI/%s/%s > /dev/null 2>&1' % (sh4multihome, target, sh4multiroot)
    rc = os.system(cmd)
    cmd = 'cp -f /etc/network/interfaces %s/SH4MultiBootI/%s/etc/network/interfaces > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    #cmd = 'cp -f /etc/passwd %s/SH4MultiBootI/%s/etc/passwd > /dev/null 2>&1' % (sh4multihome, target)
    #rc = os.system(cmd)
    cmd = 'cp -f /etc/resolv.conf %s/SH4MultiBootI/%s/etc/resolv.conf > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    cmd = 'cp -f /etc/wpa_supplicant.conf %s/SH4MultiBootI/%s/etc/wpa_supplicant.conf > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    cmd = 'rm -rf %s/SH4MultiBootI/%s/usr/lib/enigma2/python/Plugins/Extensions/HbbTV' % (sh4multihome, target)
    rc = os.system(cmd)
    cmd = 'cp -fr /usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/SH4MultiBootClient %s/SH4MultiBootI/%s/usr/lib/enigma2/python/Plugins/Extensions/ > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    cmd = 'cp -fr /usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBoot/.sh4multiboot_location %s/SH4MultiBootI/%s/usr/lib/enigma2/python/Plugins/Extensions/SH4MultiBootClient/.sh4multiboot_location > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    if installsettings == 'True':
        cmd = 'mkdir -p %s/SH4MultiBootI/%s/etc/enigma2 > /dev/null 2>&1' % (sh4multihome, target)
        rc = os.system(cmd)
        cmd = 'cp -f /etc/enigma2/* %s/SH4MultiBootI/%s/etc/enigma2/' % (sh4multihome, target)
        rc = os.system(cmd)
        cmd = 'cp -f /etc/tuxbox/* %s/SH4MultiBootI/%s/etc/tuxbox/' % (sh4multihome, target)
        rc = os.system(cmd)
    cmd = 'mkdir -p %s/SH4MultiBootI/%s/media > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    cmd = 'mkdir -p %s/SH4MultiBootI/%s/media/usb > /dev/null 2>&1' % (sh4multihome, target)
    rc = os.system(cmd)
    filename = sh4multihome + '/SH4MultiBootI/' + target + '/etc/fstab'
    filename2 = filename + '.tmp'
    out = open(filename2, 'w')
    f = open(filename, 'r')
    for line in f.readlines():
        if line.find('/dev/mtdblock2') != -1:
            line = '#' + line
        elif line.find('/dev/root') != -1:
            line = '#' + line
        out.write(line)

    f.close()
    out.close()
    os.rename(filename2, filename)
    kernelcheckflash = os.listdir('/lib/modules')
    kernelcheckmulti = os.listdir('%s/SH4MultiBootI/%s/lib/modules' % (sh4multihome, target))
    oedir = sh4multihome + '/SH4MultiBootI/' + target
    oecheck = sh4multihome + '/SH4MultiBootI/' + target + '/etc/oe-git.log'
    if kernelcheckflash == kernelcheckmulti:
        if os.path.exists(oecheck):
            print("[sh4multiboot] Use drivers from image")
        else:
            print("[sh4multiboot] Copy drivers from Flash")
	    for fdelete in glob(oedir + '/*.opk'):
		    os.remove(fdelete)
            cmd = 'mv %s/SH4MultiBootI/%s/lib/modules %s/SH4MultiBootI/%s/lib/modules1' % (sh4multihome, target, sh4multihome, target)
            rc = os.system(cmd)
            cmd = 'cp -fr /lib/modules %s/SH4MultiBootI/%s/lib' % (sh4multihome, target)
            rc = os.system(cmd)
    else:
        print("[sh4multiboot] Copy drivers")
	for fdelete in glob(oedir + '/*.opk'):
		os.remove(fdelete)
        cmd = 'mv %s/SH4MultiBootI/%s/lib/modules %s/SH4MultiBootI/%s/lib/modules1' % (sh4multihome, target, sh4multihome, target)
        rc = os.system(cmd)
        cmd = 'cp -fr /lib/modules %s/SH4MultiBootI/%s/lib' % (sh4multihome, target)
        rc = os.system(cmd)
    if os.path.exists('%s/SH4MultiBootI/%s/lib/modules1' % (sh4multihome, target)):
        print("[sh4multiboot] Search SH4 drivers")
        koLIST = []
        for fdelete in glob('%s/SH4MultiBootI/%s/lib/modules1/*.ko' % (sh4multihome, target)):
            koLIST.append(fdelete)
        for line in koLIST:
            treiberdir = "%s/SH4MultiBootI/%s/lib/modules1" % (sh4multihome, target)
            treiber = line.replace(treiberdir, '') + '\n'
            for dirpath, dirnames, filenames in os.walk("%s/SH4MultiBootI/%s/lib/modules" % (sh4multihome, target)):
                for filename in [f for f in filenames if f.endswith('.ko')]:
                    src = os.path.join(dirpath, filename)
                    if filename in treiber:
                        shutil.copy2(src, '%s/SH4MultiBootI/%s/lib/modules' % (sh4multihome, target))
    else:
        print("[sh4multiboot] OE drivers")
    tpmd = sh4multihome + '/SH4MultiBootI/' + target + '/etc/init.d/tpmd'
    if os.path.exists(tpmd):
        os.system('rm -f ' + tpmd)
    mypath = sh4multihome + '/SH4MultiBootI/' + target + '/usr/lib/opkg/info/'
    if not os.path.exists(mypath):
        mypath = sh4multihome + '/SH4MultiBootI/' + target + '/var/lib/opkg/info/'
    if not os.path.exists(mypath):
        mypath = sh4multihome + '/SH4MultiBootI/' + target + '/var/opkg/info/'
    for fn in os.listdir(mypath):
        if fn.find('kernel-image') != -1 and fn.find('postinst') != -1:
            filename = mypath + fn
            filename2 = filename + '.tmp'
            out = open(filename2, 'w')
            f = open(filename, 'r')
            for line in f.readlines():
                if line.find('/boot') != -1:
                    line = line.replace('/boot', '/boot > /dev/null 2>\\&1; exit 0')
                out.write(line)

            if f.close():
                out.close()
                os.rename(filename2, filename)
                cmd = 'chmod -R 0755 %s' % filename
                rc = os.system(cmd)
        if fn.find('-bootlogo.postinst') != -1:
            filename = mypath + fn
            filename2 = filename + '.tmp'
            out = open(filename2, 'w')
            f = open(filename, 'r')
            for line in f.readlines():
                if line.find('/boot') != -1:
                    line = line.replace('/boot', '/boot > /dev/null 2>\\&1; exit 0')
                out.write(line)

            f.close()
            out.close()
            os.rename(filename2, filename)
            cmd = 'chmod -R 0755 %s' % filename
            rc = os.system(cmd)
        if fn.find('-bootlogo.postrm') != -1:
            filename = mypath + fn
            filename2 = filename + '.tmp'
            out = open(filename2, 'w')
            f = open(filename, 'r')
            for line in f.readlines():
                if line.find('/boot') != -1:
                    line = line.replace('/boot', '/boot > /dev/null 2>\\&1; exit 0')
                out.write(line)

            f.close()
            out.close()
            os.rename(filename2, filename)
            cmd = 'chmod -R 0755 %s' % filename
            rc = os.system(cmd)
        if fn.find('-bootlogo.preinst') != -1:
            filename = mypath + fn
            filename2 = filename + '.tmp'
            out = open(filename2, 'w')
            f = open(filename, 'r')
            for line in f.readlines():
                if line.find('/boot') != -1:
                    line = line.replace('/boot', '/boot > /dev/null 2>\\&1; exit 0')
                out.write(line)

            f.close()
            out.close()
            os.rename(filename2, filename)
            cmd = 'chmod -R 0755 %s' % filename
            rc = os.system(cmd)
        if fn.find('-bootlogo.prerm') != -1:
            filename = mypath + fn
            filename2 = filename + '.tmp'
            out = open(filename2, 'w')
            f = open(filename, 'r')
            for line in f.readlines():
                if line.find('/boot') != -1:
                    line = line.replace('/boot', '/boot > /dev/null 2>\\&1; exit 0')
                out.write(line)

            f.close()
            out.close()
            os.rename(filename2, filename)
            cmd = 'chmod -R 0755 %s' % filename
            rc = os.system(cmd)

    rc = SH4MultiBootRemoveUnpackDirs()
    filename = sh4multihome + '/SH4MultiBootI/.sh4multiboot'
    out = open('/media/sh4multiboot/SH4MultiBootI/.sh4multiboot', 'w')
    out.write(target)
    out.close()
    os.system('touch /tmp/.reboot')
    rc = os.system('sync')
    os.system('reboot -p')


def SH4MultiBootRemoveUnpackDirs():
    os.chdir('/media/sh4multiboot/SH4MultiBootUpload')
    if os.path.exists('/media/sh4multiboot/SH4MultiBootUpload/enigma2'):
        shutil.rmtree('enigma2')


def SH4MultiBootExtractJFFS(source, target, zipdelete):
    SH4MultiBootRemoveUnpackDirs()
    if os.path.exists('/media/sh4multiboot/jffs2') is False:
        rc = os.system('mkdir /media/sh4multiboot/jffs2')
    sourcefile = '/media/sh4multiboot/SH4MultiBootUpload/%s.zip' % source
    if os.path.exists(sourcefile) is True:
        os.chdir('/media/sh4multiboot/SH4MultiBootUpload')
        os.system('echo "[SH4MultiBoot] Extracting image file"')
        rc = os.system('unzip ' + sourcefile)
        if zipdelete == "True":
                rc = os.system('rm -f ' + sourcefile)
        else:
                os.system('echo "[SH4MultiBoot] Keep %s for next time"' % sourcefile)
        if os.path.exists('/media/sh4multiboot/SH4MultiBootUpload/enigma2'):
            os.chdir('enigma2')
            os.system('mv -f e2jffs2.img rootfs.bin')
            GETIMAGEFOLDER = '/media/sh4multiboot/SH4MultiBootUpload/enigma2'
        print('[sh4multiboot] Extracting JFFS2 image and moving extracted image to our target')

        rootfs_path = GETIMAGEFOLDER + '/rootfs.bin'
        cmd = 'mknod /media/sh4multiboot/mtdblock7 b 31 7'
        rc = os.system(cmd)
        cmd = '/sbin/modprobe loop'
        rc = os.system(cmd)
        cmd = '/sbin/losetup /dev/loop0 ' + rootfs_path
        rc = os.system(cmd)
        cmd = '/sbin/modprobe mtdblock'
        rc = os.system(cmd)
        cmd = '/sbin/modprobe block2mtd'
        rc = os.system(cmd)
        cmd = '/bin/echo "/dev/loop0,128KiB" > /sys/module/block2mtd/parameters/block2mtd'
        rc = os.system(cmd)
        cmd = 'modprobe jffs2'
        rc = os.system(cmd)
        cmd = '/bin/mount -t jffs2 /media/sh4multiboot/mtdblock7 /media/sh4multiboot/jffs2'
        rc = os.system(cmd)
        cmd = 'cp -frp /media/sh4multiboot/jffs2/* /media/sh4multiboot/SH4MultiBootI/' + target
        rc = os.system(cmd)
        cmd = '/bin/umount /media/sh4multiboot/jffs2'
        rc = os.system(cmd)
        cmd = 'chmod -R +x /media/sh4multiboot/SH4MultiBootI/' + target
        rc = os.system(cmd)
        cmd = 'rm -f /media/sh4multiboot/jffs2'
        rc = os.system(cmd)
        cmd = 'rm -f /media/sh4multiboot/mtdblock7'
        rc = os.system(cmd)
    return 1
