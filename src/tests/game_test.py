import unittest
from main import Game

class TestGame(unittest.TestCase):
    def test_game_starts(self):
        game = Game()
        self.assertEqual(game.start_screen, True)
