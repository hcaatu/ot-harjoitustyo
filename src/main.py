import pygame
from ui import AppUI
from app import App
from upgrade import CoffeeMaker

class Main:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.app = App()
        self.ui = AppUI()
        self.app.load_game()
        self.sync()
        self.update()

    def sync(self):
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
                self.ui.timers["particle"] += 5*self.app.tickrate
                parameters = self.ui.choose_parameters()
                self.ui.particles_parameters = [
                    0, parameters[0], parameters[1], self.ui.choose_image(), 255]

            if self.ui.mouse_collide(self.ui.images["bars"], self.ui.topright, event):
                if self.ui.show_upgrades:
                    self.ui.show_upgrades = False
                else:
                    self.ui.show_upgrades = True

            if self.ui.mouse_collide(self.ui.images["coffee_maker"],
                                     self.ui.below_topright, event):
                if not self.ui.show_upgrades:
                    return
                if self.app.buy_upgrade(
                    CoffeeMaker(), self.app.cost["coffee_maker"]):
                    self.ui.cost["coffee_maker"] *= 1.2
                else:
                    self.ui.timers["no_money"] = 1.5*self.app.tickrate

        if event.type == pygame.MOUSEMOTION:
            self.ui.render_ui_elements(event)

    def update(self):
        while self.running:
            self.ui.score = self.app.score
            grey = (200, 200, 200)
            self.ui.fill_screen(grey)

            self.ui.render_upgrades()

            for event in pygame.event.get():
                self.handle_events(event)

            self.ui.window.blit(self.ui.images["coffee"], (self.ui.center))
            self.ui.window.blit(self.ui.images["bars"], (self.ui.topright))

            self.ui.render_text(self.ui.window)

            if self.ui.timers["game_saved"]:
                self.ui.render_with_timer("game_saved")
            if self.ui.timers["no_money"] and self.ui.show_textbox:
                self.ui.render_with_timer("no_money", event.pos)
            if self.ui.timers["particle"]:
                self.ui.render_particles(
                    self.ui.particles_parameters[0],
                    self.ui.particles_parameters[1],
                    self.ui.particles_parameters[2],
                    self.ui.particles_parameters[3],
                    self.ui.particles_parameters[4])
                self.ui.particles_parameters[0] += 0.5

            if self.ui.show_textbox:
                self.ui.render_textbox(self.ui.window, self.ui.textbox_pos)

            self.app.apply_profit()
            self.ui.profit = self.app.profit

            self.app.time_played += 1/self.app.tickrate

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()
