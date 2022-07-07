#!/bin/bash

display_number=$(xrandr | grep -c " connected")

if [[ display_number -eq 2 ]]; then
    notify-send "Doble pantalla"

    xrandr --output HDMI-1-3 --auto --primary --pos 0x0 &
    xrandr --output eDP-1 --auto --pos 2560x360 &
else
    notify-send "Modo portátil"
    xrandr --output HDMI-1-3 --off &
	xrandr --output eDP-1 --auto &
fi
