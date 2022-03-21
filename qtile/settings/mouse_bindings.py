from libqtile.command import lazy
from libqtile.config import Drag

from .key_bindings import mod

bring_front_click = False
cursor_warp = False
follow_mouse_focus = True

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]