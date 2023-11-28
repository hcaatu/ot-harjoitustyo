from upgrade import CoffeeMaker

class App:
    def __init__(self):
        self.score = 0
        self.tickrate = 60
        self.upgrades = {"coffee_maker": 0}
        self.cost = {"coffee_maker": CoffeeMaker().cost}
        self.profit = None

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
