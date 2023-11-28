import unittest
from ui import AppUI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = AppUI()
    
    def test_screen_correct_resolution(self):
        self.assertEqual(self.ui.resolution, (1280, 720))