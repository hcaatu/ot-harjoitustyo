import pygame
import os
from app import App

# path to the directory of this file
dirname = os.path.dirname(__file__)

class AppUI:
    def __init__(self):
        pygame.init()
        self.resolution = (1260, 720)
        
        self.window = pygame.display.set_mode(self.resolution)

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "coffee.png")
        )
        self.icon = self.image
        self.big_icon = pygame.transform.scale_by(self.icon, [1.2, 1.2])

        self.icon_w = self.icon.get_width()
        self.icon_h = self.icon.get_height()
        
        print(self.get_center(self.icon))

        self.center = self.get_center(self.icon)
        self.icon_coords = [self.center[0], self.center[0] + self.icon_w, self.center[1], self.center[1] + self.icon_h]
    
    def fill_screen(self, color):
        self.window.fill(color)

    def get_center(self, icon):
        center = (self.resolution[0]/2 - icon.get_width()/2, self.resolution[1]/2 - icon.get_height()/2)
        return center
    
"""
    def update(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_a:
                        self.score += 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    
                    if icon_coords[0] < event.pos[0] < icon_coords[1] and icon_coords[2] < event.pos[1] < icon_coords[3]:
                        self.score += 1

            if self.icon.get_rect().collidepoint(pygame.mouse.get_pos()):
                self.icon = self.big_icon
            else:
                self.icon = self.image

            grey = (200, 200, 200)
            self.fill_screen(grey)

            self.window.blit(self.icon, (self.center))

            font = pygame.font.SysFont("Arial", 24)
            counter = font.render(f"Score: {str(self.score)}", True, (255, 0, 0))
            self.window.blit(counter, (0, 0))

            pygame.display.update()
            self.clock.tick()
            """

"""
    def load_images(self):
        dirname = os.path.dirname(__file__)
        self.images = {}
        for name in ["logo"]:
            self.images[name] = pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            )
"""

