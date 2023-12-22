"""Module containing the available upgrades.
"""
# not yet in the game
class InstantCoffee:
    def __init__(self):
        self.name = "instant_coffee"
        self.cost = 1000
        self.profit = 0
        self.click_power = 10

class CoffeeMaker:
    def __init__(self):
        self.name = "coffee_maker"
        self.cost = 10
        self.profit = 1

class AeroPress:
    def __init__(self):
        self.name = "aeropress"
        self.cost = 100
        self.profit = 10
