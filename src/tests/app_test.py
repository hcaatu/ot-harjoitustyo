import unittest
from app import App
from upgrade import CoffeeMaker

class TestUI(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_constructor_functions_sets_correct_values(self):
        self.assertEqual(self.app.score, 0)
        self.assertEqual(self.app.tickrate, 60)
        self.assertEqual(self.app.profit, None)

    def test_buy_upgrade(self):
        score = 10
        upgrade = CoffeeMaker()
        self.app.buy_upgrade(upgrade, upgrade.cost)
        
