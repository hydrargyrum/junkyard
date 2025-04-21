#!/bin/sh
# SPDX-License-Identifier: WTFPL
# explicitly don't set -e: we want to go as far as possible

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id)/bus

# screen
xscreensaver-command --suspend && sleep 1
xset dpms force off

# password databases: keepassxc
/usr/lib/qt6/bin/qdbus org.keepassxc.KeePassXC.MainWindow /keepassxc org.keepassxc.KeePassXC.MainWindow.lockAllDatabases
#/usr/lib/qt6/bin/qdbus org.keepassxc.KeePassXC.MainWindow /keepassxc org.keepassxc.KeePassXC.MainWindow.exit
# password databases: gpg
killall -HUP gpg-agent

# music
playerctl pause --all-players
