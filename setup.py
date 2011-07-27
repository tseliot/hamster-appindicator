#!/usr/bin/env python
from distutils.core import setup

import subprocess, glob, os.path
import os

#mo_files = []
## HACK: make sure that the mo files are generated and up-to-date
#subprocess.call(["make", "-C", "po", "build-mo"])
#for filepath in glob.glob("po/mo/*/LC_MESSAGES/*.mo"):
#    lang = filepath[len("po/mo/"):]
#    targetpath = os.path.dirname(os.path.join("share/locale",lang))
#    mo_files.append((targetpath, [filepath]))

setup(
    name="hamster-indicator",
    author="Alberto Milone",
    author_email="albertomilone@gmail.com",
    maintainer="Alberto Milone",
    maintainer_email="albertomilone@gmail.com",
    url="https://github.com/tseliot/hamster-appindicator",
    license="'GPLv3+'",
    description="Appindicator for Hamster",
    #packages=["NvidiaDetector"],
    data_files=[("share/icons/ubuntu-mono-dark/apps/24", glob.glob("data/icons/ubuntu-mono-dark/24x24/*")),
                ("share/icons/ubuntu-mono-dark/apps/scalable", glob.glob("data/icons/ubuntu-mono-dark/scalable/*")),
                ("share/icons/ubuntu-mono-light/apps/24", glob.glob("data/icons/ubuntu-mono-light/24x24/*")),
                ("share/icons/ubuntu-mono-light/apps/scalable", glob.glob("data/icons/ubuntu-mono-light/scalable/*")),
                ("share/icons/hicolor/24x24", glob.glob("data/icons/hicolor/24x24/*")),
                ("share/icons/hicolor/scalable", glob.glob("data/icons/hicolor/scalable/*")),
                ("share/gconf/schemas", glob.glob("data/*.schemas")),
                ],# + mo_files,
    scripts=["hamster-indicator"],
)
