import unittest
import pygame
from index import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.UI = UI()

    def test_UI_starts_properly(self):
        self.assertEqual(self.UI.resolution, (640, 480))
        self.assertEqual(self.UI.window, pygame.display)