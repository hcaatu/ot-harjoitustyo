import unittest
from game_loop import GameLoop

class GameLoopTest(unittest.TestCase):
    def setUp(self):
        self.loop = GameLoop()

    def test_sync(self):
        self.loop._sync()
        self.assertEqual(self.loop.ui.score, self.loop.app.score)
        self.assertEqual(self.loop.ui.profit, self.loop.app.profit)
        self.assertEqual(self.loop.ui.upgrades, self.loop.app.upgrades)
        self.assertEqual(self.loop.ui.cost, self.loop.app.cost)

    def test_game_loop(self):
        self.loop.running = False
        self.loop.start()
        self.assertEqual(self.loop.ui.timers, {"game_saved": 0, "coffee_maker": 0, "aeropress": 0, "golden": 0})
