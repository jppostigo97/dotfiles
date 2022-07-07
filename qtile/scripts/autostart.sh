#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

feh --bg-fill $HOME/Pictures/purple-pink-bgs/pc/main.jpg &

# SXHKD for keybindings
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &
# Tray items and init important stuff
run pamac-tray &
run nm-applet &
run volumeicon &
blueberry-tray &
run variety &
run xfce4-power-manager &
numlockx on &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

# Autostart apps
run notion-app-enhanced &
run google-chrome-stable &
