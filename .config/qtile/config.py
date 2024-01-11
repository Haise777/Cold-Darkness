# If you are looking for configuring things by yourself, refer to the 'settings' directory
# settings/keymapsconf.py - Mapping of keybinds
# settings/screenconf.py  - Qtile bar
# settings/layoutsconf.py - Window and modes
# settings/groupsconf.py  - Workspaces
# settings/hooks.py       - Event hooks

from settings.groupsconf import groups
from settings.keymapsconf import keys
from settings.layoutsconf import layouts, floating_layout
from settings.screenconf import screens, widget_defaults
from settings.hooks import autostart, floating_dialogs

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
