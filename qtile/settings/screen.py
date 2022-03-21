from libqtile import bar
from libqtile.config import Screen

from .widget_list import widgets_list

screens = [Screen(top=bar.Bar(widgets=widgets_list, size=32, opacity=0.9)),
        Screen(top=bar.Bar(widgets=widgets_list, size=32, opacity=0.9))]
