from libqtile.command import lazy
from libqtile.config import Group, Key, Match

from .key_bindings import keys, mod

groups = [
    Group("", matches=[Match(wm_class=["google-chrome-stable", "firefox"])]), # web
    Group("", matches=[Match(wm_class=["code"])]), # code
    Group(""), # terminal
    Group(""), #files
    Group("", matches=[Match(wm_class=["notion-app-enhanced"])]), # tasks
    Group(""), # administrations
    Group(""), # media
    Group(""), # crypto
    Group(""), # security
    Group("") # messaging
]

for i, group in enumerate(groups):
    actual = str(i + 1) if i < 9 else str(0)
    keys.extend([
        Key([mod], actual, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual, lazy.window.togroup(group.name))
    ])
