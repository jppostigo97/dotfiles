from libqtile import widget
from .colors import colors
from .general import home

from . import arcobattery

widgets_list = [
    widget.GroupBox(font="Noto Sans Mono",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 6,
            padding_x = 5,
            borderwidth = 4,
            disable_drag = True,
            active = colors[5],
            inactive = colors[10],
            rounded = False,
            highlight_color = colors[12],
            highlight_method = "line",
            this_current_screen_border = colors[8],
            foreground = colors[5],
            background = colors[1]
            ),
    widget.Sep(
            linewidth = 1,
            padding = 12,
            foreground = colors[2],
            background = colors[1]
            ),
    widget.CurrentLayout(
            font = "Noto Sans",
            fontsize = 14,
            foreground = colors[5],
            background = colors[1]
            ),
    widget.Sep(
            linewidth = 1,
            padding = 12,
            foreground = colors[2],
            background = colors[1]
            ),
    widget.WindowName(font="Noto Sans",
            fontsize = 14,
            foreground = colors[5],
            background = colors[1],
            ),
    widget.Systray(
            background=colors[1],
            icon_size=20,
            padding = 4
            ),
    arcobattery.BatteryIcon(
        padding=0,
        scale=0.70,
        y_poss=2,
        theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
        update_interval = 5,
        background = colors[1]
    ),
    widget.TextBox(
        font="FontAwesome",
        text="  ",
        foreground=colors[3],
        background=colors[1],
        padding = 0,
        fontsize=20
    ),
    widget.Clock(
        foreground = colors[5],
        background = colors[1],
        fontsize = 14,
        format="%H:%M"
    ),
    widget.TextBox(
        font="FontAwesome",
        text="   ",
        foreground=colors[3],
        background=colors[1],
        padding = 0,
        fontsize=20
    ),
    widget.Clock(
        foreground = colors[5],
        background = colors[1],
        fontsize = 14,
        format="%d/%m"
    ),
]
