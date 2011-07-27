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

# Install icons for hicolor ubuntu-mono-light and ubuntu-mono-dark
for theme in hicoloro ubuntu-mono-light ubuntu-mono-dark; do
    install_icon data/icons/$theme/24x24/hamster-applet-active.png hamster-applet-active $theme
    install_icon data/icons/$theme/24x24/hamster-applet-inactive.png hamster-applet-inactive $theme
done
