#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# Replace Qtile default keybindings
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &

run variety &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

run volumeicon &
run google-chrome-stable
run code
run notion-app-nativefier
