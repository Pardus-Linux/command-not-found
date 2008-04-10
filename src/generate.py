#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# This python script generates the packages db needed by command-not-found.
# Must be run on buildfarm.

import glob
import os
import cPickle
import sys
import pisi

# Append a local copy of trunk/pisi for using Pisi API without having
# root privileges on buildfarm.
sys.path.append("pisi/")

if __name__ == "__main__":
    d = {}
    file_list = glob.glob("/var/cache/pisi/packages/*.pisi")

    for p in file_list:
        print "Processing %s.." % p
        for f in filter(lambda x:x.type=="executable", pisi.package.Package(p).get_files().list):
            d[os.path.join("/", f.path)] = (os.path.basename(p).rstrip(".pisi")).rsplit("-", 3)[0]

    o = open("packages.db", "wb")
    cPickle.Pickler(o, protocol=2)
    cPickle.dump(d, o, protocol=2)
    o.close()

