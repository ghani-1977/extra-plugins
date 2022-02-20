#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from . import sh4multiboot

if len(sys.argv) < 5:
    print("[ex_init] Not enough parameters for SH4MultiBoot")
else:
    sh4multiboot.SH4MultiBootMainEx(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
