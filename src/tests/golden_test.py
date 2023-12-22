import unittest
import pygame
from golden import Golden

class TestGolden(unittest.TestCase):
    def setUp(self):
        self.golden = Golden()

    def test_constructor_function_sets_correct_values(self):
        self.assertEqual(self.golden.height, 138)
        self.assertEqual(self.golden.width, 78)
        self.assertEqual(self.golden.tickrate, 60)

    def test_generate_with_cheat(self):
        pos = self.golden.generate(True)
        self.assertNotEqual(pos, False)

    def test_generate(self):
        while True:
            pos = self.golden.generate()
            if not pos:
                break
        self.assertEqual(pos, False)
