#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.

import sys
import os
import locale
import cPickle

import gettext
__trans = gettext.translation("command-not-found", fallback=True)
_ = __trans.ugettext

try:
    if __name__ == "__main__":
        try:
            # unpickle data
            d = cPickle.Unpickler(open("/var/command-not-found/packages.db", "rb")).load()

            cmd = sys.argv[1]

            # check path
            for dir in os.getenv("PATH").split(":"):
                cmd_path = os.path.join(dir, os.path.basename(cmd))
                if d.has_key(cmd_path):
                    break

            # if found in loop, we'll get the package name
            # if not, it will throw KeyError.
            package = d[cmd_path]

            # inform the user

            print _("The program '%s' is not installed on your system.") % package,

            if os.geteuid() == 0:
                # Has uid 0, can install the package
                print _("You can install it using package manager or by typing:")
                print "pisi it %s" % package

            elif "wheel" in os.popen("groups").read().split():
                # Can sudo
                print _("You can install it using package manager or by typing:")
                print "sudo pisi it %s" % package

            else:
                print _("You can install it using package manager.")

        except KeyError:
            pass
finally:
    sys.exit(127)
