from random import random, randint
from image_loader import ImageLoader

class Golden:
    def __init__(self):
        self.image = ImageLoader().load_golden_coffee()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tickrate = 60

    def generate(self, cheat=False):
        chance = 1/(30*self.tickrate)
        if random() <= chance or cheat:
            pos = (randint(0, 1280-self.width), randint(0, 720-self.height))
            return pos
        return None
    
    def render_golden(self, window, img, pos, alpha):
        img.set_alpha(alpha)
        window.blit(img, pos)
