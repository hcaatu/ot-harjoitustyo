import pygame
from upgrade import CoffeeMaker

class App:
    def __init__(self):
        self.score = 0
        self.tickrate = 60
        self.upgrades = {"coffee_maker" : 0}
        self.profit = None

    def buy_upgrade(self, upgrade):
        if self.score >= upgrade.cost:
            self.score -= upgrade.cost
            self.upgrades[upgrade.name] += 1
            print(self.upgrades)
            self.calculate_profit()
            print("yes")
        elif self.score < upgrade.cost:
            print("no")

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