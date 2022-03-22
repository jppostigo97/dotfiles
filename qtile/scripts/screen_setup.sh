#!/bin/bash

display_number=$(xrandr | grep -c " connected")

if [[ display_number -eq 2 ]]; then
    notify-send "Configurando pantalla secundaria"

    second_monitor=$(xrandr | grep " connected" | cut -f2 -d$'\n' | cut -f1 -d ' ')

	xrandr --output eDP-1 --auto &
	eval $(xrandr --output $second_monitor --auto) &
else
    notify-send "Configurando monitor portátil"
	xrandr --output eDP-1 --auto &
fi
