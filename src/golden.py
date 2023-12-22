from random import random, randint
from image_loader import ImageLoader

class Golden:
    """Generates the golden coffee clickable icon on screen with random chance.
    """
    def __init__(self):
        self.image = ImageLoader().load_golden_coffee()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tickrate = 60
        print(self.width)
        print(self.height)

    def generate(self, cheat=False):
        """Generates the golden coffee with random chance, but approx once every half minutes.

        Args:
            cheat (bool, optional): If true, coffee appears always. Defaults to False.

        Returns:
            False: if random chance doesn't occur. 
            pos (tuple): The coordinates of the icon, when it happens to generate.
        """
        chance = 1/(30*self.tickrate)
        if random() <= chance or cheat:
            pos = (randint(0, 1280-self.width), randint(0, 720-self.height))
            return pos
        return False
