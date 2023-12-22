import unittest
import pygame
from image_loader import ImageLoader

class TestImageLoader(unittest.TestCase):
    def setUp(self):
        self.loader = ImageLoader()

    def test_load_images(self):
        images = self.loader.load_images()
        self.assertEqual(len(images), 8)
        for name, image in images.items():
            self.assertEqual(type(image), pygame.Surface)

    def test_load_particles(self):
        images = self.loader.load_particles()
        self.assertEqual(len(images), 3)
        for name, image in images.items():
            self.assertEqual(type(image), pygame.Surface)

    def test_load_golden_coffee(self):
        image = self.loader.load_golden_coffee()
        self.assertEqual(type(image), pygame.Surface)
