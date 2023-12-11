import pygame
from ui import AppUI
from app import App
from upgrades import CoffeeMaker
from particles import Particle

class Main:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.app = App()
        self.ui = AppUI()
        self.app.load_game()
        self.update()

    def sync(self):
        self.ui.score = self.app.score
        self.ui.profit = self.app.profit
        self.ui.upgrades = self.app.upgrades
        self.ui.cost = self.app.cost

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

            if event.key == pygame.K_a:  # cheat
                if self.app.buy_upgrade(
                    CoffeeMaker(), self.app.cost["coffee_maker"]):
                    self.ui.cost["coffee_maker"] *= 1.2
                else:
                    self.ui.timers["coffee_maker"] = 1.5*self.app.tickrate

            if event.key == pygame.K_s:
                self.app.save_game()
                self.ui.timers["game_saved"] = 2*self.app.tickrate

            # cheat
            if event.key == pygame.K_g:
                self.app.score = 1000

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.ui.mouse_collide(self.ui.images["coffee"], self.ui.pos["center"], event):
                self.app.apply_score()
                self.ui.timers["particle"] += 2*self.app.tickrate
                self.ui.particles.append(Particle())

            if self.ui.mouse_collide(self.ui.images["bars"], self.ui.pos["upgrade0"], event):
                if self.ui.show["upgrades"]:
                    self.ui.show["upgrades"] = False
                else:
                    self.ui.show["upgrades"] = True

            for upgrade in self.app.data:
                if self.ui.mouse_collide(self.ui.images[upgrade.name],
                                        self.ui.pos[upgrade.name], event):
                    if not self.ui.show["upgrades"]:
                        return
                    if self.app.buy_upgrade(
                        upgrade, self.app.cost[upgrade.name]):
                        self.ui.cost[upgrade.name] *= 1.1
                    else:
                        self.ui.timers[upgrade.name] = 1.5*self.app.tickrate

        if event.type == pygame.MOUSEMOTION:
            self.ui.render_motion_elements(event)

    def update(self):
        while self.running:
            self.sync()
            self.ui.fill_screen()

            for event in pygame.event.get():
                self.handle_events(event)

            self.ui.render_text()
            self.ui.render_elements()

            if self.ui.timers["game_saved"]:
                self.ui.render_with_timer("game_saved")
            if self.ui.timers["particle"]:
                for p in self.ui.particles:
                    self.ui.render_particles(p)
            for upgrade in self.app.data:
                if self.ui.timers[upgrade.name] and self.ui.show["textbox"]:
                    self.ui.render_with_timer(upgrade.name, event.pos)

            if self.ui.show["textbox"]:
                self.ui.render_textbox(self.ui.pos["textbox"])

            self.app.apply_profit()
            self.ui.profit = self.app.profit

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()
