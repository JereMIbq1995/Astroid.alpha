from astroid.cast.astroid import Astroid
from genie.script.action import UpdateAction
from genie.cast.actor import Actor
import random

from pygame import image

SPAWN_INTERVAL = 5000

class SpawnAstroidsAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._last_spawn = 0
        self._window_size = window_size
        self._astroid_spawn = False

    def execute(self, actors, actions, clock, callback):
        #  and self._astroid_spawn == False
        if (clock._frames - self._last_spawn) >= SPAWN_INTERVAL:
            # Generate a random position on top of the screen
            lower = int(self._window_size[0] / 8)
            higher = int(self._window_size[0] - lower)

            start_pos_y = 0
            start_pos_x = random.randint(lower, higher)

            # Generate a reasonable velocity
            vel_x = 1
            if start_pos_x > self._window_size[0] / 2:
                vel_x *= -1
            vel_y = 4

            # Pick a random type of astroid: Small, Medium, Large
            as_type = random.randint(0,3)
            size : tuple = (0, 0)
            if as_type == 1:
                size = (75, 75)
            elif as_type == 2:
                size = (120, 120)
            else:
                size = (150, 150)


            # spawn an astroid
            astroid = Astroid("", width=size[0], height=size[1], x = start_pos_x, y = start_pos_y, vx = vel_x, vy = vel_y, rotation_vel=1)
            callback.add_actor(astroid)

            # set last_spawn to current frame
            self._last_spawn = clock._frames