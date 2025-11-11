# Submarine Flappy Bird - Simplified Version

A simplified version of Flappy Bird transformed into a submarine-themed game.

## What Was Changed

### ✅ Simplified Assets
- **Removed**: Multiple submarine colors, obstacle types, and background variations
- **Kept**: Only yellow submarine, pink coral obstacles, and shallow ocean background
- **Replaced**: Bird sprites with submarine sprites (yellow bird → yellow submarine)

### ✅ Simplified Code
- **constants.py**: Removed randomization arrays, kept only single asset paths
- **images.py**: Removed randomization logic, loads assets directly
- **pipe.py**: Simplified class structure, removed unnecessary methods
- **player.py**: Kept submarine theme comments and logic

### ✅ Removed Files
- Multiple sprite variants (blue/red submarines, different coral types, extra backgrounds)
- Test scripts and sprite creation utilities
- Unused obstacle variants

## How to Run Locally

### Option 1: Quick Setup (Recommended)
```bash
# Navigate to the submarine directory
cd submarine

# Create virtual environment and install
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pygame

# Run the game
python3 main.py
```

### Option 2: System-wide Install
```bash
cd submarine
pip3 install pygame
python3 main.py
```

## Game Features
- **Yellow submarine** with 3 animation frames (up, mid, down)
- **Pink coral obstacles** (top and bottom)
- **Ocean background** (shallow water)
- **Original Flappy Bird physics** and gameplay
- **Press SPACE** to make the submarine rise

## File Structure (Simplified)
```
submarine/
├── main.py                     # Game entry point
├── src/
│   ├── utils/
│   │   ├── constants.py        # Simple asset paths (no arrays)
│   │   └── images.py          # Direct asset loading
│   └── entities/
│       ├── player.py          # Submarine player
│       ├── pipe.py            # Coral obstacles
│       └── background.py      # Ocean background
└── assets/sprites/
    ├── submarine/              # 3 yellow submarine sprites
    ├── obstacles/             # Pink coral (top + bottom)
    └── backgrounds/           # Single ocean background
```

## Controls
- **SPACE BAR**: Make submarine rise
- **Mouse Click**: Alternative control
- **ESC**: Exit game

The game maintains the original challenging Flappy Bird gameplay but with a clean, simple submarine theme!