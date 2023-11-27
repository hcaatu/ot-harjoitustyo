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
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    if event.key == pygame.K_a:
                        self.app.buy_upgrade(CoffeeMaker())

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ui.icon_coords[0] < event.pos[0] < self.ui.icon_coords[1] and self.ui.icon_coords[2] < event.pos[1] < self.ui.icon_coords[3]:
                        self.app.score += 1

                # Make the icon larger when hovering mouse over

                if event.type == pygame.MOUSEMOTION:
                    if self.ui.icon_coords[0] < event.pos[0] < self.ui.icon_coords[1] and self.ui.icon_coords[2] < event.pos[1] < self.ui.icon_coords[3]:
                        # print(event.pos)
                        self.ui.icon = self.ui.big_icon
                        self.ui.center = (self.ui.resolution[0]/2 - self.ui.icon.get_width()/2, self.ui.resolution[1]/2 - self.ui.icon.get_height()/2)
                    else:
                        self.ui.icon = self.ui.image
                        self.ui.center = (self.ui.resolution[0]/2 - self.ui.icon.get_width()/2, self.ui.resolution[1]/2 - self.ui.icon.get_height()/2)
                        
            
            grey = (200, 200, 200)
            self.ui.fill_screen(grey)

            self.ui.window.blit(self.ui.icon, (self.ui.center))

            font = pygame.font.SysFont("Arial", 24)
            counter = font.render(f"Score: {str(int(self.app.score))}", True, (255, 0, 0))
            self.ui.window.blit(counter, (0, 0))

            self.app.apply_profit()

            pygame.display.update()
            self.clock.tick(self.app.tickrate)

Main()