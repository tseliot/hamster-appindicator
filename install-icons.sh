#!/bin/bash
#
# Author: Izidor Matušov <izidor.matusov@gmail.com>
# Date:   22.07.2011

install_icon() {
    file="$1"
    name="$2"
    theme="$3"

    xdg-icon-resource install --theme "$theme" --novendor --size 24 "$file" "$name"
}

# Inactive icons for ubuntu-mono-light and ubuntu-mono-dark
install_icon icons/hamster-applet-inactive-dark.png hamster-applet-inactive ubuntu-mono-light
install_icon icons/hamster-applet-inactive-light.png hamster-applet-inactive ubuntu-mono-dark

# Active icons for ubuntu-mono-light and ubuntu-mono-dark
install_icon icons/hamster-applet-active-dark.png hamster-applet-active ubuntu-mono-light
install_icon icons/hamster-applet-active-light.png hamster-applet-active ubuntu-mono-dark

# Active icons for the hicolor theme
install_icon icons/hamster-applet-active.png hamster-applet-active hicolor
install_icon icons/hamster-applet-inactive.png hamster-applet-inactive hicolor
