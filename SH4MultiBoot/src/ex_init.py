#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import sh4multiboot

if len(sys.argv) < 5:
    pass
else:
    sh4multiboot.SH4MultiBootMainEx(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
