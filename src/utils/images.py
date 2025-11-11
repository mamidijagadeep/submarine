import pygame

from .constants import SUBMARINE, BACKGROUND, OBSTACLE_TOP, OBSTACLE_BOTTOM


class Images:
    def __init__(self) -> None:
        # Load UI elements
        self.numbers = [
            pygame.image.load(f"assets/sprites/{num}.png").convert_alpha()
            for num in range(10)
        ]

        # Load game screens
        self.game_over = pygame.image.load("assets/sprites/gameover.png").convert_alpha()
        self.welcome_message = pygame.image.load("assets/sprites/message.png").convert_alpha()
        self.base = pygame.image.load("assets/sprites/base.png").convert_alpha()

        # Load submarine sprites
        self.player = (
            pygame.image.load(SUBMARINE[0]).convert_alpha(),
            pygame.image.load(SUBMARINE[1]).convert_alpha(),
            pygame.image.load(SUBMARINE[2]).convert_alpha(),
        )

        # Load background
        self.background = pygame.image.load(BACKGROUND).convert()

        # Load obstacles
        self.pipe = (
            pygame.image.load(OBSTACLE_TOP).convert_alpha(),
            pygame.image.load(OBSTACLE_BOTTOM).convert_alpha(),
        )
