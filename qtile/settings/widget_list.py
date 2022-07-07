from libqtile import widget
from .colors import color
from .general import home

from . import arcobattery

def left_arrow(pre_color, post_color):
    return widget.TextBox(
        text = '\uE0B2',
        padding = 0,
        fontsize = 26,
        background = post_color,
        foreground = pre_color
    )

def right_arrow(pre_color, post_color):
    return widget.TextBox(
        text = '\uE0B0',
        padding = 0,
        fontsize = 26,
        background = post_color,
        foreground = pre_color
    )

left_side_widgets = [
    widget.GroupBox(
        font="Noto Sans Mono",
        fontsize = 16,

        background = color["grey"],
        foreground = color["white"],
        
        highlight_method = "block",
        active = color["white"],
        inactive = color["not_grey"],

        this_current_screen_border = color["purple"],
        this_screen_border = color["dark_purple"],
        other_current_screen_border = color["comp2_light"],
        other_screen_border = color["comp2"],

        margin_y = 3,
        margin_x = 0,
        padding_x = 6,
        padding_y = 6,
        
        rounded = True,
        disable_drag = True
    ),
    right_arrow(
        color["grey"],
        color["light_grey"]
    ),
    widget.CurrentLayout(
        font = "Noto Sans",
        fontsize = 14,

        background = color["light_grey"],
        foreground = color["comp1_light"],

        padding = 8
    ),
    right_arrow(
        color["light_grey"], 
        color["grey"]
    ),
    widget.WindowName(
        font = "Noto Sans",
        fontsize = 14,
        
        background = color["grey"],
        foreground = color["comp2_light"],

        padding = 12
    )
]

right_side_widgets = [
    left_arrow(
        color["comp2"], 
        color["grey"]
    ),
    arcobattery.Battery(
        font = "Noto Sans",

        background = color["comp2"],

        padding = 8,

        update_interval = 5
    ),
    left_arrow(
        color["comp1"],
        color["comp2"]
    ),
    widget.TextBox(
        font = "FontAwesome",
        fontsize = 20,

        background = color["comp1"],
        foreground = color["white"],

        padding = 0,

        text = "   "
    ),
    widget.Clock(
        fontsize = 14,

        background = color["comp1"],
        foreground = color["white"],
        
        format="%H:%M  -  %d/%m  "
    )
]

full_widgets_list = left_side_widgets + [
        widget.Systray(
            background = color["grey"],
            icon_size = 20,
            padding = 4
        ),
        widget.Spacer(
            background = color["grey"],
            length = 8
        )
    ] + right_side_widgets

second_widgets_list = left_side_widgets + right_side_widgets
