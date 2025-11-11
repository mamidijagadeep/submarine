#!/usr/bin/env python3
"""
Create submarine-themed sprites for the Flappy Bird game transformation.
This script generates pixel art sprites programmatically.
"""

import os
from PIL import Image, ImageDraw


def create_submarine_sprites():
    """Create 9 submarine sprites (3 colors × 3 animations)"""

    # Define colors for submarines
    colors = {
        'yellow': {'body': (255, 204, 0), 'window': (150, 150, 200), 'propeller': (100, 100, 100)},
        'blue': {'body': (0, 120, 255), 'window': (200, 200, 255), 'propeller': (50, 50, 80)},
        'red': {'body': (220, 20, 20), 'window': (255, 200, 200), 'propeller': (80, 40, 40)}
    }

    # Animation states
    animations = ['up', 'mid', 'down']

    # Create directory if it doesn't exist
    os.makedirs('assets/sprites/submarine', exist_ok=True)

    for color_name, color in colors.items():
        for anim in animations:
            img = Image.new('RGBA', (34, 24), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            # Main submarine body (elongated oval)
            body_y = 8
            if anim == 'up':
                body_y = 6  # Slightly higher for rising
            elif anim == 'down':
                body_y = 10  # Slightly lower for falling

            # Draw main body
            draw.ellipse([2, body_y, 32, body_y + 12], fill=color['body'])

            # Draw conning tower/periscope
            draw.rectangle([14, body_y - 3, 20, body_y], fill=color['body'])
            draw.rectangle([17, body_y - 5, 18, body_y - 3], fill=color['propeller'])

            # Draw window (circular)
            draw.ellipse([8, body_y + 3, 12, body_y + 7], fill=color['window'])
            draw.ellipse([22, body_y + 3, 26, body_y + 7], fill=color['window'])

            # Draw propeller
            if anim == 'mid':  # Spinning propeller
                draw.ellipse([28, body_y + 4, 32, body_y + 8], fill=color['propeller'])
                draw.line([30, body_y + 2, 30, body_y + 10], fill=(255, 255, 255), width=1)
                draw.line([28, body_y + 6, 32, body_y + 6], fill=(255, 255, 255), width=1)
            else:
                draw.ellipse([28, body_y + 4, 32, body_y + 8], fill=color['propeller'])

            # Add bubbles for rising animation
            if anim == 'up':
                draw.ellipse([5, body_y - 2, 7, body_y], fill=(200, 200, 255, 180))
                draw.ellipse([15, body_y - 4, 17, body_y - 2], fill=(180, 180, 255, 150))
                draw.ellipse([25, body_y - 1, 27, body_y + 1], fill=(220, 220, 255, 160))

            # Save the sprite
            filename = f'assets/sprites/submarine/{color_name}-{anim}.png'
            img.save(filename)
            print(f'Created {filename}')


def create_obstacle_sprites():
    """Create coral reef and rock formation obstacles"""

    os.makedirs('assets/sprites/obstacles', exist_ok=True)

    # Coral sprites
    coral_colors = [(255, 107, 107), (255, 142, 83), (255, 182, 142)]

    for i, color in enumerate(coral_colors):
        # Top coral (inverted for top pipes)
        img = Image.new('RGBA', (52, 320), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Create organic coral shape
        draw.ellipse([0, 280, 52, 320], fill=color)  # Base
        draw.polygon([(0, 280), (10, 200), (20, 240), (30, 180), (40, 220), (52, 280)], fill=color)
        draw.ellipse([8, 170, 18, 190], fill=(255, 120, 120))
        draw.ellipse([32, 150, 42, 170], fill=(255, 130, 130))

        filename = f'assets/sprites/obstacles/coral-pink-top.png'
        img.save(filename)
        print(f'Created {filename}')

        # Bottom coral (normal orientation)
        img_bottom = img.transpose(Image.FLIP_TOP_BOTTOM)
        filename = f'assets/sprites/obstacles/coral-pink-bottom.png'
        img_bottom.save(filename)
        print(f'Created {filename}')

    # Rock formations
    rock_colors = [(128, 128, 128), (80, 80, 80)]

    for i, color in enumerate(rock_colors):
        # Top rocks
        img = Image.new('RGBA', (52, 320), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Create angular rock shape
        draw.polygon([(0, 280), (15, 150), (35, 200), (52, 280), (52, 320), (0, 320)], fill=color)
        draw.polygon([(10, 150), (20, 100), (30, 150)], fill=(color[0]-20, color[1]-20, color[2]-20))

        filename = f'assets/sprites/obstacles/rocks-gray-top.png' if i == 0 else f'assets/sprites/obstacles/rocks-basalt-top.png'
        img.save(filename)
        print(f'Created {filename}')

        # Bottom rocks
        img_bottom = img.transpose(Image.FLIP_TOP_BOTTOM)
        filename = f'assets/sprites/obstacles/rocks-gray-bottom.png' if i == 0 else f'assets/sprites/obstacles/rocks-basalt-bottom.png'
        img_bottom.save(filename)
        print(f'Created {filename}')


def create_background_sprites():
    """Create ocean background sprites"""

    os.makedirs('assets/sprites/backgrounds', exist_ok=True)

    # Ocean depth variations
    backgrounds = [
        ('ocean-shallow', (26, 127, 160), (13, 93, 122)),  # Light blue
        ('ocean-medium', (8, 61, 122), (4, 41, 82)),     # Medium blue
        ('ocean-deep', (8, 61, 94), (4, 31, 62))          # Dark blue
    ]

    for name, top_color, bottom_color in backgrounds:
        img = Image.new('RGBA', (288, 512), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Create gradient background
        for y in range(512):
            ratio = y / 512
            r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
            g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
            b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
            draw.line([(0, y), (288, y)], fill=(r, g, b))

        # Add some light rays
        for i in range(5):
            x = 50 + i * 60
            draw.polygon([(x, 0), (x + 20, 0), (x + 10, 512), (x - 10, 512)],
                        fill=(255, 255, 255, 20))

        # Add some bubbles
        for i in range(15):
            x = (i * 73) % 288
            y = (i * 137) % 512
            size = 3 + (i % 4)
            draw.ellipse([x, y, x + size, y + size], fill=(255, 255, 255, 80))

        filename = f'assets/sprites/backgrounds/{name}.png'
        img.save(filename)
        print(f'Created {filename}')


if __name__ == '__main__':
    create_submarine_sprites()
    create_obstacle_sprites()
    create_background_sprites()
    print('All sprites created successfully!')