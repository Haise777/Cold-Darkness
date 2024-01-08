from libqtile import bar, widget
from libqtile.config import Screen
from colourthemes.darkness import colors

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=15,
    padding=5,
    foreground=colors["foreground"],
    background=colors["background"],
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
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
                    #foreground = colourthemes["fg"],
                    #background = colourthemes["red"],
                    #hide_unused=True,
                    ),
                widget.Prompt(),
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
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    update_interval=1800,
                    display_format="+{updates} ",
                    foreground=colors["update"],
                    background=colors["background"],
                    colour_have_updates=colors["update"],
                    colour_no_updates=colors["noupdate"],
                    ),
                widget.CurrentLayout(),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
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
                widget.CPU(
                    format=' {load_percent:>3.0f}%'
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                widget.Memory(
                    format='RAM:{MemUsed:>5.0f}{mm}',
                    update_interval=5,
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors["separator"],
                    padding=10
                    ),
                widget.Clock(format="%a %d, %b - %R"),
                widget.Spacer(length=10)
            ],
            30,  # bar height
            margin=[0, 0, 0, 0],  # Draw top and bottom borders   [ top, right, bottom, left ]
        ),
    ),
]

