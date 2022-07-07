from libqtile import bar
from libqtile.config import Screen

from .widget_list import full_widgets_list, second_widgets_list

screens = [
    Screen(
        top=bar.Bar(
            margin = 4,
            opacity = 1,
            size = 32,
            widgets = full_widgets_list
        )
    ),
    Screen(
        top=bar.Bar(
            margin = 4,
            opacity = 1,
            size = 32,
            widgets = second_widgets_list
        )
    )
]
