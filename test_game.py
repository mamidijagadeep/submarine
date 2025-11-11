#!/usr/bin/env python3
"""
Test script to verify the submarine game can load assets correctly
without requiring a display.
"""

import os
import sys

# Set SDL to use a dummy video driver to avoid display issues
os.environ['SDL_VIDEODRIVER'] = 'dummy'

try:
    # Test importing pygame
    import pygame
    pygame.init()
    print("✓ Pygame imported successfully")

    # Test importing game modules
    sys.path.append('src')
    from src.utils.constants import PLAYERS, BACKGROUNDS, PIPES
    print("✓ Constants imported successfully")

    from src.utils.images import Images
    print("✓ Images module imported successfully")

    # Test loading assets
    images = Images()
    print("✓ Images loaded successfully")

    # Test submarine assets
    print(f"✓ Found {len(PLAYERS)} submarine variants:")
    for i, submarine in enumerate(PLAYERS):
        print(f"  - Submarine {i+1}: {submarine[0].split('/')[-1]} (3 animations)")

    # Test background assets
    print(f"✓ Found {len(BACKGROUNDS)} ocean backgrounds:")
    for bg in BACKGROUNDS:
        print(f"  - {bg.split('/')[-1]}")

    # Test obstacle assets
    print(f"✓ Found {len(PIPES)} obstacle types:")
    for obstacle in PIPES:
        print(f"  - {obstacle.split('/')[-1]}")

    # Test image dimensions
    player_img = images.player[0]
    print(f"✓ Submarine sprite dimensions: {player_img.get_width()}x{player_img.get_height()}")

    obstacle_img = images.pipe[0]
    print(f"✓ Obstacle sprite dimensions: {obstacle_img.get_width()}x{obstacle_img.get_height()}")

    bg_img = images.background
    print(f"✓ Background sprite dimensions: {bg_img.get_width()}x{bg_img.get_height()}")

    print("\n🎮 All tests passed! The submarine game should work correctly.")

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)