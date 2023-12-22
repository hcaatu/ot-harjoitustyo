import pygame
from ui import AppUI
from app import App
from golden import Golden
from event_handler import EventHandler

class GameLoop:
    """Used to start the game loop and check user inputs inside the loop.
    """
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.app = App()
        self.ui = AppUI()
        self.golden = Golden()
        self.handler = EventHandler()
        self.running = True
        self.app.load_game()

    def sync(self):
        """Sends values from the app module to the UI module.
        """
        self.ui.score = self.app.score
        self.ui.profit = self.app.profit
        self.ui.upgrades = self.app.upgrades
        self.ui.cost = self.app.cost

    def start(self):
        """The game loop itself, uses the UI module to update screen.

        The function handles user inputs using the event handler module and updates
        attributes that are constantly changing, also checking if some UI element needs
        to be rendered from the different timers.
        """
        while self.running:
            self.sync()

            for event in pygame.event.get():
                print(event)
                self.running = self.handler.handle_events(event, self.ui, self.app)

            self.ui.fill_screen()
            self.ui.render_text()
            self.ui.render_elements()

            if self.ui.timers["game_saved"]:
                self.ui.render_with_timer("game_saved")
            for p in self.ui.particles:
                self.ui.render_particles(p)
            for upgrade in self.app.data:
                if self.ui.timers[upgrade.name] and self.ui.show["textbox"]:
                    self.ui.render_with_timer(upgrade.name, event.pos)

            if self.ui.show["textbox"]:
                self.ui.render_textbox(self.ui.pos["textbox"])

            if self.ui.timers["golden"]:
                self.ui.render_golden_coffee()
            else:
                golden_pos = self.golden.generate()
                if golden_pos:
                    self.ui.timers["golden"] += 7*self.app.tickrate
                    self.ui.pos["golden"] = golden_pos

            self.app.apply_profit()

            pygame.display.update()
            self.clock.tick(self.app.tickrate)
