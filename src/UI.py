import pygame
import os

# path to the directory of this file
dirname = os.path.dirname(__file__)

class AppUI:
    def __init__(self):
        pygame.init()
        self.resolution = (1280, 720)
        
        self.window = pygame.display.set_mode(self.resolution)

        self.show_upgrades = False

        self.images = []
        filenames = ["coffee", "bars", "coffee_maker", "textbox"]
        for name in filenames:
            self.images.append(pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            ))

        self.images_rect = []
        for image in self.images:
            self.images_rect.append(image.get_rect())

        self.coffee = self.images[0]
        self.bars = self.images[1]
        self.coffeemaker = self.images[2]
        self.textbox = self.images[3]

        self.big_icon = pygame.transform.scale_by(self.coffee, [1.2, 1.2])
        
        print(self.get_center(self.coffee))
        
        self.center = self.get_center(self.coffee)
        #self.coffee_coords = self.get_coords(self.coffee, self.center)

        safezone = 20
        self.topright = (self.resolution[0] - self.bars.get_width() - safezone, safezone)

        self.below_topright = (self.topright[0], self.topright[1] + self.bars.get_height() + 2)
    
    def mouse_collide(self, icon, pos, event):
        icon_coords = [pos[0], pos[0] + icon.get_width(), pos[1], pos[1] + icon.get_height()]
        if icon_coords[0] < event.pos[0] < icon_coords[1] and icon_coords[2] < event.pos[1] < icon_coords[3]:
            return True
        return False


    def fill_screen(self, color):
        self.window.fill(color)

    def get_center(self, icon):
        center = (self.resolution[0]/2 - icon.get_width()/2, self.resolution[1]/2 - icon.get_height()/2)
        return center
    
"""
    def load_images(self):
        dirname = os.path.dirname(__file__)
        self.images = {}
        for name in ["logo"]:
            self.images[name] = pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            )
"""

