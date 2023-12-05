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

    def update(self):
        while self.running:
            self.ui.score = self.app.score
            grey = (200, 200, 200)
            self.ui.fill_screen(grey)

            self.ui.render_upgrades()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    if event.key == pygame.K_a:  # cheat
                        if self.app.score >= self.app.cost["coffee_maker"]:
                            self.app.buy_upgrade(
                                CoffeeMaker(), self.app.cost["coffee_maker"])
                            self.ui.cost["coffee_maker"] *= 1.2

                    if event.key == pygame.K_s:
                        self.app.save_game()
                        self.ui.timers["game_saved"] = 2*self.app.tickrate

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ui.mouse_collide(self.ui.coffee, self.ui.center, event):
                        self.app.score += 1

                    if self.ui.mouse_collide(self.ui.bars, self.ui.topright, event):
                        if self.ui.show_upgrades:
                            self.ui.show_upgrades = False
                        else:
                            self.ui.show_upgrades = True

                    if self.ui.mouse_collide(self.ui.coffeemaker, self.ui.below_topright, event):
                        if self.ui.show_upgrades:
                            if self.app.score >= self.app.cost["coffee_maker"]:
                                self.app.buy_upgrade(
                                    CoffeeMaker(), self.app.cost["coffee_maker"])
                                self.ui.cost["coffee_maker"] *= 1.2
                            else:
                                self.ui.timers["no_money"] = 1.5*self.app.tickrate

                if event.type == pygame.MOUSEMOTION:
                    self.ui.render_ui_elements(event)

            self.ui.window.blit(self.ui.coffee, (self.ui.center))
            self.ui.window.blit(self.ui.bars, (self.ui.topright))

            self.ui.render_text(self.ui.window)

            if self.ui.timers["game_saved"]:
                self.ui.render_with_timer("game_saved")
            if self.ui.timers["no_money"] and self.ui.show_textbox:
                if event.type in (
                    pygame.MOUSEBUTTONUP,
                    pygame.MOUSEBUTTONDOWN,
                    pygame.MOUSEMOTION):
                    self.ui.render_with_timer("no_money", event.pos)

            if self.ui.show_textbox:
                self.ui.render_textbox(self.ui.window, self.ui.textbox_pos)

            self.app.apply_profit()
            self.ui.profit = self.app.profit

            self.app.time_played += 1/self.app.tickrate

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()
