import os
import pygame
from upgrade import CoffeeMaker

# path to the directory of this file
dirname = os.path.dirname(__file__)


class AppUI:
    def __init__(self):
        pygame.init()
        self.resolution = (1280, 720)
        self.window = pygame.display.set_mode(self.resolution)
        self.score = 0
        self.profit = 0
        self.show_upgrades = False
        self.show_textbox = False
        self.timers = {"game_saved": 0, "no_money": 0}
        self.font = pygame.font.SysFont("Arial", 24)

        self.images = []
        filenames = ["coffee", "bars", "coffee_maker", "textbox"]
        for name in filenames:
            self.images.append(pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            ))

        self.coffee = self.images[0]
        self.bars = self.images[1]
        self.coffeemaker = self.images[2]
        self.textbox = self.images[3]

        self.big_icon = pygame.transform.scale_by(self.coffee, [1.2, 1.2])

        self.upgrades = {"coffee_maker": 0}
        self.cost = {"coffee_maker": CoffeeMaker().cost}

        self.center = self.get_center(self.coffee)

        self.safezone = 20
        self.topright = (
            self.resolution[0] - self.bars.get_width() - self.safezone, self.safezone)
        self.below_topright = (
            self.topright[0], self.topright[1] + self.bars.get_height() + 2)

    def render_text(self, window):
        black = (0, 0, 0)
        font = self.font
        counter = font.render(f"Coffee: {str(int(self.score))}", True, black)
        window.blit(counter, (self.safezone, 10))
        score_per_second = font.render(
            f"{str(self.profit)} coffee/second", True, black)
        window.blit(score_per_second, (self.safezone, 36))

    def render_with_timer(self, msg, pos=None):
        black = (0, 0, 0)
        size = 28
        font = pygame.font.SysFont("Arial", size)
        if msg == "game_saved":
            pos = (self.safezone, self.resolution[1] - size - self.safezone)
            text = font.render("Game saved!", True, black)
        elif msg == "no_money":
            pos = (self.textbox_pos[0] + 5, self.textbox_pos[1] - 35)
            text = font.render("Not enough coffee!", True, black)
            if self.score >= self.cost["coffee_maker"]:
                self.timers[msg] = 0
                return
        self.window.blit(text, pos)
        self.timers[msg] -= 1

    def render_textbox(self, window, pos):
        margin = 15
        leading = 26
        black = (0, 0, 0)
        font = self.font
        window.blit(self.textbox, pos)
        window.blit((font.render(f"Coffee maker", True, black)),
                    [margin + i for i in pos])
        if self.upgrades["coffee_maker"] != 0:
            count = ": " + {self.upgrades["coffee_maker"]}
            window.blit((font.render(count, True, black)),
                        (132 + pos[0], margin + pos[1]))
# assigning variable before using it in f-string fixes syntax error in wsl, hence pylint comment
        decimal_format = "{:.2f}".format(self.cost["coffee_maker"]) # pylint: disable=consider-using-f-string
        window.blit((font.render(f"Cost: {decimal_format}", True, black)), (
            pos[0] + margin, pos[1] + margin + leading))
        window.blit((
            font.render(f"Produces {CoffeeMaker().profit} coffee per second", True, black)), (
            pos[0] + 15, pos[1] + margin + 2 * leading))
        italic = pygame.font.SysFont("Arial", 24, False, True)
        window.blit((italic.render("Makes more coffee", True, black)),
                    (pos[0] + 25, pos[1] + 105))

    def mouse_collide(self, icon, pos, event):
        icon_coords = [pos[0], pos[0] + icon.get_width(), pos[1],
                       pos[1] + icon.get_height()]
        if icon_coords[0] < event.pos[0] < icon_coords[1]:
            if icon_coords[2] < event.pos[1] < icon_coords[3]:
                return True
        return False
    
    def render_ui_elements(self, event):
        if self.mouse_collide(self.coffee, self.center, event):
            self.coffee = self.big_icon
            self.center = self.get_center(self.coffee)
        elif self.mouse_collide(self.coffeemaker, self.below_topright, event):
            if self.show_upgrades:
                self.textbox_pos = (
                    event.pos[0] - self.images[3].get_width(), event.pos[1])
                self.show_textbox = True
        else:
            self.coffee = self.images[0]
            self.center = self.get_center(self.coffee)
            self.show_textbox = False

    def render_upgrades(self):
        grey_box = pygame.surface.Surface(
            (self.images[2].get_width(), self.images[2].get_height()))
        grey_box.fill((255,255,255))
        grey_box.set_alpha(100)
        if self.show_upgrades:
            self.window.blit(self.coffeemaker, self.below_topright)
            if self.score < self.cost["coffee_maker"]:
                self.window.blit(grey_box, self.below_topright)


    def fill_screen(self, color):
        self.window.fill(color)

    def get_center(self, icon):
        center = (self.resolution[0]/2 - icon.get_width()/2,
                  self.resolution[1]/2 - icon.get_height()/2)
        return center
