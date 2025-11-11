# list of all possible submarines (tuple of 3 animation states)
SUBMARINES = (
    # red submarine
    (
        "assets/sprites/submarine/red-up.png",
        "assets/sprites/submarine/red-mid.png",
        "assets/sprites/submarine/red-down.png",
    ),
    # blue submarine
    (
        "assets/sprites/submarine/blue-up.png",
        "assets/sprites/submarine/blue-mid.png",
        "assets/sprites/submarine/blue-down.png",
    ),
    # yellow submarine
    (
        "assets/sprites/submarine/yellow-up.png",
        "assets/sprites/submarine/yellow-mid.png",
        "assets/sprites/submarine/yellow-down.png",
    ),
)

# Keep original for backward compatibility
PLAYERS = SUBMARINES

# list of backgrounds
BACKGROUNDS = (
    "assets/sprites/background-day.png",
    "assets/sprites/background-night.png",
)

# list of pipes
PIPES = (
    "assets/sprites/pipe-green.png",
    "assets/sprites/pipe-red.png",
)
