import subprocess
from os import path

from settings.general import wmname, qtile_scripts_path
from settings.key_bindings import keys
from settings.layout import auto_fullscreen, focus_on_window_activation, floating_layout, floating_types, layouts
from settings.mouse_bindings import bring_front_click, cursor_warp, follow_mouse_focus, mouse
from settings.screen import screens
from settings.workspace import groups

from libqtile import hook

dgroups_key_binder = None
dgroups_app_rules = []

@hook.subscribe.startup_once
def start_once():
    subprocess.call([path.join(qtile_scripts_path, "autostart.sh")])
    subprocess.call([path.join(qtile_scripts_path, "screen_setup.sh")])

@hook.subscribe.restart
def restart_hook():
    subprocess.call([path.join(qtile_scripts_path, "screen_setup.sh")])
