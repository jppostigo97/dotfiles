from libqtile import bar
from libqtile.config import Screen

from .widget_list import full_widgets_list, second_widgets_list

screens = [Screen(top=bar.Bar(widgets=full_widgets_list, size=32, opacity=0.9))
        ,
        Screen(top=bar.Bar(widgets=second_widgets_list, size=32, opacity=0.9))
        ]
