from astroid.cast.ship import Ship
from genie.script.action import OutputAction
from genie.services.PygameScreenService import WHITE, PygameScreenService

class DrawFrameAction(OutputAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._window_size = window_size
        self._screen_service = PygameScreenService(window_size)

    def get_priority(self):
        return super().get_priority()
    
    def set_priority(self, priority):
        return super().set_priority(priority)

    def execute(self, actors, actions, clock, callback):
        self._screen_service.fill_screen(WHITE)
        for actor in actors:
            # Black for astroids, blue for ship
            color = (0,0,255) if isinstance(actor, Ship) else (0,0,0)
            self._screen_service.draw_rectangle(actor.get_position(), actor.get_width(), actor.get_height(), color, border_width = 5)
        self._screen_service.update_screen()