#!/usr/bin/env python3
"""
Test the simplified submarine game
"""
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
pygame.init()
pygame.display.set_mode((1, 1))

try:
    # Test constants
    from src.utils.constants import SUBMARINE, BACKGROUND, OBSTACLE_TOP, OBSTACLE_BOTTOM
    print("✓ Constants loaded")
    print(f"  - Submarine sprites: {len(SUBMARINE)}")
    print(f"  - Background: {BACKGROUND}")
    print(f"  - Obstacles: top={OBSTACLE_TOP}, bottom={OBSTACLE_BOTTOM}")

    # Test images loading
    from src.utils.images import Images
    images = Images()
    print("✓ Images loaded successfully")

    # Test submarine animation
    print(f"  - Submarine dimensions: {images.player[0].get_width()}x{images.player[0].get_height()}")
    print(f"  - Background dimensions: {images.background.get_width()}x{images.background.get_height()}")
    print(f"  - Obstacle top dimensions: {images.pipe[0].get_width()}x{images.pipe[0].get_height()}")
    print(f"  - Obstacle bottom dimensions: {images.pipe[1].get_width()}x{images.pipe[1].get_height()}")

    print("\n🎮 Simplified submarine game is ready!")
    print("Run with: python3 main.py")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()