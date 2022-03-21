#!/bin/bash

display_number=$(xrandr | grep -c " connected")

if [[ display_number -eq 2 ]]; then
    notify-send "Configurando pantalla secundaria"
	xrandr --output eDP-1 --auto &
	xrandr --output HDMI-1-1 --auto &
else
    notify-send "Configurando monitor portátil"
    xrandr --output HDMI-1-1 --off &
	xrandr --output eDP-1 --auto &
fi
