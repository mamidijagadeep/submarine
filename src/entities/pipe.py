import random
from typing import List

from ..utils import GameConfig
from .entity import Entity


class Obstacle(Entity):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vel_x = -5

    def draw(self) -> None:
        self.x += self.vel_x
        super().draw()


class Obstacles(Entity):
    upper: List[Obstacle]
    lower: List[Obstacle]

    def __init__(self, config: GameConfig) -> None:
        super().__init__(config)
        self.pipe_gap = 120
        self.top = 0
        self.bottom = self.config.window.viewport_height
        self.upper = []
        self.lower = []
        self.spawn_initial_pipes()

    def tick(self) -> None:
        if self.can_spawn_pipes():
            self.spawn_new_pipes()
        self.remove_old_pipes()

        for up_pipe, low_pipe in zip(self.upper, self.lower):
            up_pipe.tick()
            low_pipe.tick()

    def stop(self) -> None:
        for obstacle in self.upper + self.lower:
            obstacle.vel_x = 0

    def can_spawn_obstacles(self) -> bool:
        last = self.upper[-1]
        if not last:
            return True

        return self.config.window.width - (last.x + last.w) > last.w * 2.5

    def spawn_new_obstacles(self):
        # add new obstacle when first obstacle is about to touch left of screen
        upper, lower = self.make_random_obstacles()
        self.upper.append(upper)
        self.lower.append(lower)

    def remove_old_obstacles(self):
        # remove first obstacle if its out of the screen
        for obstacle in self.upper:
            if obstacle.x < -obstacle.w:
                self.upper.remove(obstacle)

        for obstacle in self.lower:
            if obstacle.x < -obstacle.w:
                self.lower.remove(obstacle)

    def spawn_initial_obstacles(self):
        upper_1, lower_1 = self.make_random_obstacles()
        upper_1.x = self.config.window.width + upper_1.w * 3
        lower_1.x = self.config.window.width + upper_1.w * 3
        self.upper.append(upper_1)
        self.lower.append(lower_1)

        upper_2, lower_2 = self.make_random_obstacles()
        upper_2.x = upper_1.x + upper_1.w * 3.5
        lower_2.x = upper_1.x + upper_1.w * 3.5
        self.upper.append(upper_2)
        self.lower.append(lower_2)

    def make_random_obstacles(self):
        """returns a randomly generated obstacle"""
        # y of gap between upper and lower obstacle
        base_y = self.config.window.viewport_height

        gap_y = random.randrange(0, int(base_y * 0.6 - self.pipe_gap))
        gap_y += int(base_y * 0.2)
        obstacle_height = self.config.images.pipe[0].get_height()
        obstacle_x = self.config.window.width + 10

        upper_obstacle = Obstacle(
            self.config,
            self.config.images.pipe[0],
            obstacle_x,
            gap_y - obstacle_height,
        )

        lower_obstacle = Obstacle(
            self.config,
            self.config.images.pipe[1],
            obstacle_x,
            gap_y + self.pipe_gap,
        )

        return upper_obstacle, lower_obstacle


# Backward compatibility aliases
Pipe = Obstacle
Pipes = Obstacles
