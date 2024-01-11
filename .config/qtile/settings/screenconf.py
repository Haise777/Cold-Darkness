from libqtile import bar, widget
from libqtile.config import Screen
from colorpalett import colors

# Default values of the bar widgets
widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=15,
    padding=5,
    foreground=colors["foreground"],
    background=colors["background"],
)

screens = [
    Screen(
        # Qtile bar settings
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                # DateTime
                widget.Clock(format="%a %b %d - %R"),
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
                    this_current_screen_border=colors["current"],  # current active workspace color - MAIN
                    this_screen_border=colors["current"],
                    other_current_screen_border=colors["background"],
                    other_screen_border=colors["background"],
                    urgent_border=colors["highlight"],
                    urgent_text=colors["highlight"],
                    #foreground = colorthemes["fg"],
                    #background = colorthemes["red"],
                    #hide_unused=True,
                    ),
                #widget.WindowName(),
                widget.Spacer(
                    length=bar.STRETCH
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
                # Available updates counter
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    update_interval=1800,
                    display_format="+{updates} ",
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
                # Download speed
                widget.Net(
                    prefix='M',
                    update_interval=2,
                    format='↓{down:>5.2f}{down_suffix}',
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # CPU
                widget.CPU(
                    format=' {load_percent:>3.0f}%'
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                # Memory
                widget.Memory(
                    format='RAM:{MemUsed:>5.0f}{mm}',
                    update_interval=5,
                    ),
                widget.Spacer(length=10)
            ],
            30,  # bar height
            margin=[5, 5, 0, 5],  # Draw top and bottom borders   [ top, right, bottom, left ]
        ),
    ),
]
