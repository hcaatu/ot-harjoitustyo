import unittest
from unittest.mock import MagicMock
import pygame

# Fix for importing issues on WSL

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())
sys.path.append(myDir)

from UI import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.ui = UI()

    def test_UI_starts_properly(self):
        self.assertEqual(self.ui.resolution, (640, 480))
        self.assertEqual(self.ui.window, pygame.display)
        self.ui.update.assert_called_once()

    def test_UI_closes_properly(self):
        ui = UI()
        ui.running = True
        pygame.event.get = MagicMock(return_value=[pygame.event.Event(pygame.QUIT)])

        ui.update()

        self.assertFalse(ui.running)
