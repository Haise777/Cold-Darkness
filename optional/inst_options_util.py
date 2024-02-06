#github: https://github.com/Haise777

bar_widgets = {
    "centered": f'''\
                widget.Spacer(length=10),
                # DateTime
                widget.Clock(format="%R - %a %b %d"),
                widget.Spacer(
                    length=bar.STRETCH
                    ),
                # Workspace group
                widget.GroupBox(
                    fontsize=16,
                    highlight_method="text",
                    active=colors["active"],  # not current active workspace
                    inactive=colors["inactive"],
                    rounded=False,
                    disable_drag=True,
                    highlight_color=colors["highlight"],
                    this_current_screen_border=colors["current"],  # current active workspace color
                    this_screen_border=colors["current"],
                    other_current_screen_border=colors["background"],
                    other_screen_border=colors["background"],
                    urgent_border=colors["highlight"],
                    urgent_text=colors["highlight"],
                    ),
                #widget.WindowName(),
                widget.Spacer(
                    length=bar.STRETCH
                    ),
                widget.Chord(
                    chords_colors={{
                        "launch": ("#ff0000", "#ffffff"),
                    }},
                    name_transform=lambda name: name.upper(),
                    ),
                # Available updates counter
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    update_interval=1800,
                    display_format="+{{updates}} ",
                    foreground=colors["update"],
                    background=colors["background"],
                    colour_have_updates=colors["update"],
                    colour_no_updates=colors["noupdate"],
                    ),
                # Current layout mode
                widget.CurrentLayout(),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                widget.Volume(fmt='⪡ {{}}'),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # Download speed
                widget.Net(
                    prefix='M',
                    update_interval=2,
                    format='↓{{down:>5.2f}}{{down_suffix}}',
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # Memory
                widget.Memory(
                    format='RAM:{{MemUsed:>5.0f}}{{mm}}',
                    update_interval=5,
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # CPU
                widget.CPU(
                    format=' {{load_percent:>3.0f}}%'
                    ),
                widget.Spacer(length=10)
''',

    "on_side": f'''\
                widget.Spacer(length=10),
                # Workspace group
                widget.GroupBox(
                    fontsize=16,
                    highlight_method="text",
                    active=colors["active"],  # not current active workspace
                    inactive=colors["inactive"],
                    rounded=False,
                    disable_drag=True,
                    highlight_color=colors["highlight"],
                    this_current_screen_border=colors["current"],  # current active workspace color
                    this_screen_border=colors["current"],
                    other_current_screen_border=colors["background"],
                    other_screen_border=colors["background"],
                    urgent_border=colors["highlight"],
                    urgent_text=colors["highlight"],
                    ),
                #widget.WindowName(),
                widget.Spacer(
                    length=bar.STRETCH
                    ),
                widget.Chord(
                    chords_colors={{
                        "launch": ("#ff0000", "#ffffff"),
                    }},
                    name_transform=lambda name: name.upper(),
                    ),
                # Available updates counter
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    update_interval=1800,
                    display_format="+{{updates}} ",
                    foreground=colors["update"],
                    background=colors["background"],
                    colour_have_updates=colors["update"],
                    colour_no_updates=colors["noupdate"],
                    ),
                # Current layout mode
                widget.CurrentLayout(),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                widget.Volume(fmt='⪡ {{}}'),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # Download speed
                widget.Net(
                    prefix='M',
                    update_interval=2,
                    format='↓{{down:>5.2f}}{{down_suffix}}',
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # CPU
                # Memory
                widget.Memory(
                    format='RAM:{{MemUsed:>5.0f}}{{mm}}',
                    update_interval=5,
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # CPU
                widget.CPU(
                    format=' {{load_percent:>3.0f}}%'
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # DateTime
                widget.Clock(format="%a %b %d - %R"),
                widget.Spacer(length=10)
'''
}
