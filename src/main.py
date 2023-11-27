import pygame
from UI import AppUI
from app import App
from upgrade import CoffeeMaker

class Main:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.app = App()
        self.ui = AppUI()
        self.update()

    def update(self):
        while self.running:
            
            grey = (200, 200, 200)
            self.ui.fill_screen(grey)

            if self.ui.show_upgrades:
                self.ui.window.blit(self.ui.coffeemaker, (self.ui.below_topright))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    if event.key == pygame.K_a: # cheat 
                        self.app.buy_upgrade(CoffeeMaker(), self.app.cost["coffee_maker"]) 
                        print(self.app.upgrades["coffee_maker"])

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
                            self.app.buy_upgrade(CoffeeMaker(), self.app.cost["coffee_maker"]) # fix this

                # Make the icon larger when hovering mouse over

                if event.type == pygame.MOUSEMOTION:
                    
                    if self.ui.mouse_collide(self.ui.coffee, self.ui.center, event):
                        # print(event.pos)
                        self.ui.coffee = self.ui.big_icon
                        self.ui.center = (self.ui.resolution[0]/2 - self.ui.coffee.get_width()/2, self.ui.resolution[1]/2 - self.ui.coffee.get_height()/2) # make function

                    elif self.ui.mouse_collide(self.ui.coffeemaker, self.ui.below_topright, event):
                        if self.ui.show_upgrades:
                            textbox_pos = (event.pos[0] - self.ui.images[3].get_width(), event.pos[1])
                            self.ui.show_textbox = True
    
                    else:
                        self.ui.coffee = self.ui.images[0]
                        self.ui.center = (self.ui.resolution[0]/2 - self.ui.coffee.get_width()/2, self.ui.resolution[1]/2 - self.ui.coffee.get_height()/2)
                        self.ui.show_textbox = False

            self.ui.window.blit(self.ui.coffee, (self.ui.center))
            self.ui.window.blit(self.ui.bars, (self.ui.topright))


            font = pygame.font.SysFont("Arial", 24)
            
            black = (0, 0, 0)
            counter = font.render(f"Coffee: {str(int(self.app.score))}", True, black)
            self.ui.window.blit(counter, (10, 10))
            score_per_second = font.render(f"{str(self.app.profit)} coffee/second", True, black)
            self.ui.window.blit(score_per_second, (10, 36))

            if self.ui.show_textbox:
                self.ui.window.blit(self.ui.textbox, textbox_pos)
                self.ui.window.blit((font.render(f"Coffee maker", True, black)), [15 + i for i in textbox_pos])
                self.ui.window.blit((font.render(f"Cost: {"{:.2f}".format(self.app.cost["coffee_maker"])}", True, black)), (textbox_pos[0] + 15, textbox_pos[1] + 41))
                font = pygame.font.SysFont("arialblack", 26)
                font.set_italic(font)
                self.ui.window.blit((font.render(f"Makes more coffee", True, black)), (textbox_pos[0] + 25, textbox_pos[1] + 80))

            self.app.apply_profit()

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()