from genie_core.director import Director
from genie_plugins.services.PygameKeyboardService import PygameKeyboardService

from genie_core.cast.actor import Actor
from genie_core.cast.actors import Actors
from genie_core.cast.Body import Body
from genie_core.cast.Image import Image

from genie_core.script.action import Action
from genie_core.script.actions import Actions

from cast.PlayerControlledTrait import PlayerControlledTrait
from script.DrawFrameAction import DrawFrameAction
from script.HandleInputAction import HandleInputAction
from script.MoveBodiesAction import MoveBodiesAction
from script.SpawnAstroidsAction import SpawnAstroidsAction

W_SIZE = (500, 700)
START_POSITION = 200, 250
SHIP_WIDTH = 40
SHIP_LENGTH = 55

def main():

    # Create a director
    director = Director()

    # Create all the actors, including the player
    cast = Actors()

    # Create the player
    player = Actor()
    player.add_trait(Body(W_SIZE[0]/2 - SHIP_LENGTH/2, W_SIZE[1]/10 * 9, width = SHIP_LENGTH, height = SHIP_WIDTH))
    player.add_trait(Image("assets/spaceship/spaceship_yellow.png", 0.12, 180))
    player.add_trait(PlayerControlledTrait())

    # Give actor(s) to the cast
    cast.add_actor(player)

    # Create all the actions
    script = Actions()

    # Create input actions
    handle_input = HandleInputAction(1, PygameKeyboardService())

    # Create update actions
    move_bodies = MoveBodiesAction(1)
    spawn_astroid = SpawnAstroidsAction(1, W_SIZE)

    # Create output actions
    draw_frame = DrawFrameAction(1, W_SIZE)

    # Give action(s) to the script
    script.add_action(handle_input)
    script.add_action(move_bodies)
    script.add_action(spawn_astroid)
    script.add_action(draw_frame)

    # Give the cast and script to the dirrector by calling direct_scene.
    # direct_scene then runs the main game loop:
    director.direct_scene(cast, script)

if __name__ == "__main__":
    main()