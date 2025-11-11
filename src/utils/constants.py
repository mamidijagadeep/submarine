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

# list of ocean backgrounds
OCEAN_BACKGROUNDS = (
    "assets/sprites/backgrounds/ocean-shallow.png",
    "assets/sprites/backgrounds/ocean-medium.png",
    "assets/sprites/backgrounds/ocean-deep.png",
)

# Keep original for backward compatibility
BACKGROUNDS = OCEAN_BACKGROUNDS

# list of underwater obstacles (top sprites)
OBSTACLES_TOP = (
    "assets/sprites/obstacles/coral-pink-top.png",
    "assets/sprites/obstacles/rocks-gray-top.png",
    "assets/sprites/obstacles/rocks-basalt-top.png",
    "assets/sprites/obstacles/coral-brain-top.png",
)

# list of underwater obstacles (bottom sprites)
OBSTACLES_BOTTOM = (
    "assets/sprites/obstacles/coral-pink-bottom.png",
    "assets/sprites/obstacles/rocks-gray-bottom.png",
    "assets/sprites/obstacles/rocks-basalt-bottom.png",
    "assets/sprites/obstacles/coral-brain-bottom.png",
)

# Keep original for backward compatibility
OBSTACLES = OBSTACLES_TOP
PIPES = OBSTACLES_TOP
