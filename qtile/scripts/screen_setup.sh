#!/bin/bash

display_number=$(xrandr | grep -c " connected")

if [[ display_number -eq 2 ]]; then
    notify-send "Configurando pantalla secundaria"

    eval $(/home/jppostigo/scripts/left.sh &)
else
    notify-send "Configurando monitor portátil"
	xrandr --output eDP-1 --auto &
fi
