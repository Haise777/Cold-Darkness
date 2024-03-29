#github: https://github.com/Haise777

from libqtile import layout
from libqtile.config import Match
from colorpalett import colors

# Default window values
layout_theme = {
    "border_width": 0,
    "margin": 5
}

# Default available layout modes // Uncomment which option you want to be available
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
    # Try more layouts by unleashing below layouts.
    #layout.MonadWide(**layout_theme),
    #layout.Columns(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=0
)
