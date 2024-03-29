#github: https://github.com/Haise777

# If you are looking for configuring things by yourself, go to the 'settings' directory
# settings/keymapsconf.py - Mapping of keybinds
# settings/screenconf.py  - Qtile bar and it's widgets
# settings/layoutsconf.py - Window and modes
# settings/groupsconf.py  - Workspaces
# settings/hooks.py       - Event hooks

from settings.groups import groups
from settings.keymaps import keys
from settings.layouts import layouts, floating_layout
from settings.screen import screens, widget_defaults
from settings.hooks import autostart, floating_dialogs


# Base Qtile configuration variables
extension_defaults = widget_defaults.copy()
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
