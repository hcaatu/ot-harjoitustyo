import unittest
import tempfile
from app import App
from upgrades import CoffeeMaker

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.score = 100
        self.file_path = tempfile.NamedTemporaryFile(delete=False).name

    def test_constructor_functions_sets_correct_values(self):
        self.assertEqual(self.app.score, 100)
        self.assertEqual(self.app.tickrate, 60)
        self.assertEqual(self.app.profit, 0)

    def test_buy_upgrade(self):
        upgrade = CoffeeMaker()

        initial_upgrades = {"coffee_maker" : 0}
        initial_score = self.app.score
        initial_cost = upgrade.cost

        self.app.buy_upgrade(upgrade, upgrade.cost)

        self.assertEqual(self.app.score, initial_score - initial_cost)
        self.assertEqual(self.app.upgrades[upgrade.name], initial_upgrades[upgrade.name] + 1)
        self.assertEqual(self.app.cost[upgrade.name], initial_cost * 1.2)
        self.assertEqual(self.app.profit, 1)

    def test_calculate_profit(self):
        upgrade = CoffeeMaker()

        self.app.buy_upgrade(upgrade, upgrade.cost)
        self.app.calculate_profit()
        self.assertEqual(self.app.profit, 1)

    def test_apply_profit(self):
        initial_score = self.app.score
        self.app.profit = 100
        self.app.apply_profit()
        self.assertEqual(self.app.score, initial_score + self.app.profit/self.app.tickrate)

    def test_profit_doesnt_apply_if_there_is_no_profit(self):
        initial_score = self.app.score
        self.app.profit = 0
        self.app.apply_profit()
        self.assertEqual(self.app.score, initial_score)

    def test_golden_click(self):
        self.app.score = 0
        self.app.golden_click()
        self.assertEqual(self.app.score, 60)
        self.app.profit = 10
        self.app.golden_click()
        self.assertEqual(self.app.score, 660)