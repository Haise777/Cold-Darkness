from libqtile import hook
import os
import subprocess

# Execute when user do the first log in
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])

# Check if a new window should be float type
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == "tk"
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True
