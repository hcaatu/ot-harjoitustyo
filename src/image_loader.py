import os
import pygame

dirname = os.path.dirname(__file__)

class ImageLoader:
    def __init__(self):
        self.images = {}
    
    def load_images(self):
        """Load images using pygame built in image.load function.

        Returns:
            self.images (dict): Contains the names and surface objects of images.
        """
        filenames = ["coffee", "bars", "coffee_maker", "textbox", "aeropress"]
        for name in filenames:
            self.images[name] = (pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            ))
        self.images["small_coffee"] = self.images["coffee"]
        self.images["big_coffee"] = pygame.transform.scale_by(self.images["coffee"], [1.2, 1.2])
        return self.images

    def load_particles(self):
        """Loads images for particle effects.

        Returns:
            self.images (dict): Contains the names and surface objects of images.
        """
        filenames = ["beans", "mug", "caffeine"]
        for name in filenames:
            self.images[name] = (pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            ))
        return self.images