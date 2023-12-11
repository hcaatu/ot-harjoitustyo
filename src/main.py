import pygame
from ui import AppUI
from app import App
from upgrade import CoffeeMaker
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
                    self.ui.timers["no_money"] = 1.5*self.app.tickrate

            if event.key == pygame.K_s:
                self.app.save_game()
                self.ui.timers["game_saved"] = 2*self.app.tickrate

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.ui.mouse_collide(self.ui.images["coffee"], self.ui.center, event):
                self.app.score += 1
                self.ui.timers["particle"] += 2*self.app.tickrate
                self.ui.particles.append(Particle())

            if self.ui.mouse_collide(self.ui.images["bars"], self.ui.topright, event):
                if self.ui.show["upgrades"]:
                    self.ui.show["upgrades"] = False
                else:
                    self.ui.show["upgrades"] = True

            if self.ui.mouse_collide(self.ui.images["coffee_maker"],
                                     self.ui.below_topright, event):
                if not self.ui.show["upgrades"]:
                    return
                if self.app.buy_upgrade(
                    CoffeeMaker(), self.app.cost["coffee_maker"]):
                    self.ui.cost["coffee_maker"] *= 1.2
                else:
                    self.ui.timers["no_money"] = 1.5*self.app.tickrate

        if event.type == pygame.MOUSEMOTION:
            self.ui.render_motion_elements(event)

    def update(self):
        while self.running:
            self.sync()
            grey = (200, 200, 200)
            self.ui.fill_screen(grey)

            for event in pygame.event.get():
                self.handle_events(event)

            self.ui.render_text()
            self.ui.render_elements()

            if self.ui.timers["game_saved"]:
                self.ui.render_with_timer("game_saved")
            if self.ui.timers["no_money"] and self.ui.show["textbox"]:
                self.ui.render_with_timer("no_money", event.pos)   
            if self.ui.timers["particle"]:
                for p in self.ui.particles:
                    self.ui.render_particles(p)

            if self.ui.show["textbox"]:
                self.ui.render_textbox(self.ui.textbox_pos)

            self.app.apply_profit()
            self.ui.profit = self.app.profit

            self.app.time_played += 1/self.app.tickrate

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()
