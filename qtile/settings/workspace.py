from libqtile.command import lazy
from libqtile.config import Group, Key

from .key_bindings import keys, mod

groups = [Group(i) for i in [
    "www", "dev", "sh", "file", "task", "adm", "media", "crypto", "sec", "msg"
]]

for i, group in enumerate(groups):
    actual = str(i + 1) if i < 9 else str(0)
    keys.extend([
        Key([mod], actual, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual, lazy.window.togroup(group.name))
    ])
