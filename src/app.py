import os
from upgrade import CoffeeMaker
from repository import SaveFile, Repository

dirname = os.path.dirname(__file__)

class App:
    def __init__(self):
        self.score = 0
        self.tickrate = 60
        self.upgrades = {"coffee_maker": 0}
        self.cost = {"coffee_maker": CoffeeMaker().cost}
        self.profit = None
        self.time_played = 0
        self.repository = Repository(os.path.join(dirname, "..", "data", "data.csv"))

    def buy_upgrade(self, upgrade, cost):
        self.score -= cost
        self.upgrades[upgrade.name] += 1
        self.cost[upgrade.name] *= 1.2
        self.calculate_profit()

    def calculate_profit(self):
        self.profit = 1
        for upgrade, count in self.upgrades.items():
            if upgrade == "coffee_maker":
                gain = CoffeeMaker().profit
            self.profit *= gain
            self.profit *= count

    def apply_profit(self):
        if self.profit:
            self.score += self.profit / self.tickrate

    def save_game(self):
        file = SaveFile(self.score, self.upgrades, self.cost, self.time_played)
        self.repository.save(file)
        return file

    def load_game(self):
        file = self.repository.load()
        self.score = file.score
        self.upgrades = file.upgrades
        self.cost = file.cost
        self.time_played = file.time_played
        self.calculate_profit()
