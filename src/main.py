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
        self.ui.cost = self.app.cost
        self.ui.profit = self.app.profit
        self.ui.upgrades = self.app.upgrades
        self.ui.cost = self.app.cost

    def update(self):
        while self.running:
            self.ui.score = self.app.score
            grey = (200, 200, 200)
            self.ui.fill_screen(grey)

            if self.ui.show_upgrades:
                self.ui.window.blit(self.ui.coffeemaker,
                                    (self.ui.below_topright))

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
                        self.ui.timer = 2 * self.app.tickrate

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

                # Make the icon larger when hovering mouse over

                if event.type == pygame.MOUSEMOTION:
                    if self.ui.mouse_collide(self.ui.coffee, self.ui.center, event):
                        self.ui.coffee = self.ui.big_icon
                        self.ui.center = self.ui.get_center(self.ui.coffee)
                    elif self.ui.mouse_collide(self.ui.coffeemaker, self.ui.below_topright, event):
                        if self.ui.show_upgrades:
                            textbox_pos = (
                                event.pos[0] - self.ui.images[3].get_width(), event.pos[1])
                            self.ui.show_textbox = True
                    else:
                        self.ui.coffee = self.ui.images[0]
                        self.ui.center = self.ui.get_center(self.ui.coffee)
                        self.ui.show_textbox = False

            self.ui.window.blit(self.ui.coffee, (self.ui.center))
            self.ui.window.blit(self.ui.bars, (self.ui.topright))

            self.ui.render_text(self.ui.window)

            if self.ui.timer:
                self.ui.render_game_saved()
                self.ui.timer -= 1

            if self.ui.show_textbox:
                self.ui.render_textbox(self.ui.window, textbox_pos)

            self.app.apply_profit()
            self.ui.profit = self.app.profit

            self.app.time_played += 1/self.app.tickrate

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()
