from genie.script.action import UpdateAction
from genie.cast.actor import Actor
import random

from pygame import image

SPAWN_INTERVAL = 2000

class SpawnAstroidsAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._last_spawn = 0
        self._window_size = window_size

    def execute(self, actors, actions, clock, callback):
        if (clock._frames - self._last_spawn) >= SPAWN_INTERVAL:
            # Generate a random position on top of the screen
            lower = int(self._window_size[0] / 8)
            higher = int(self._window_size[0] - lower)

            start_pos_y = 0
            start_pos_x = random.randint(lower, higher)

            # Generate a reasonable velocity
            vel_x = 0.1
            vel_y = 5

            # Pick a random type of astroid: Small, Medium, Large
            as_type = random.randint(0,3)
            image_path = ""
            if as_type == 1:
                image_path = "astroid/assets/astroids/astroid_large.png"
            elif as_type == 2:
                image_path = "astroid/assets/astroids/astroid_med.png"
            else:
                image_path = "astroid/assets/astroids/astroid_small.png"


            # spawn an astroid
            astroid = Actor(image_path, 1, x = start_pos_x, y = start_pos_y, vx = vel_x, vy = vel_y,)
            actors.append(astroid)

            # set last_spawn to current frame
            self._last_spawn = clock._frames