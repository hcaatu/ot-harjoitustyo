import upgrade
from repository import SaveFile, Repository

class App:
    """Class handles the funcitionality of the game.

    Class provides functions for calculating score, upgrade costs and other gameplay-related.
    Class imports the Repository class to provide saving and loading functions.
    """
    def __init__(self):
        """Constructor function that assigns intial values.
        """
        self.score = 0
        self.tickrate = 60
        self.data = [upgrade.CoffeeMaker(), upgrade.AeroPress()]
        self.upgrades = {"coffee_maker": 0, "aeropress": 0}
        self.cost = {"coffee_maker": self.data[0].cost,
                     "aeropress": self.data[1].cost}
        self.click = 1
        self.profit = 0
        self.time_played = 0
        self.repository = Repository("data/data.csv")

    def buy_upgrade(self, upgrade, cost):
        """Used to check if there is enough score to buy an upgrade, and changing the in-game values after buying.

        Args:
            upgrade (Upgrade object): Contains upgrade data
            cost (dict): Contains the mutable costs of all upgrades

        Returns:
            bool: True/False depending if there is enough score to buy
        """
        success = self.score >= cost
        if success:
            self.score -= cost
            self.upgrades[upgrade.name] += 1
            self.cost[upgrade.name] *= 1.2
            self.calculate_profit()
        return success

    def calculate_profit(self):
        """Calculates coffee per second based on purchased upgrades.
        """
        self.profit = 0
        for upgrade in self.data:
            if self.upgrades[upgrade.name] != 0:
                self.profit += upgrade.profit * self.upgrades[upgrade.name]

    def apply_score(self):
        """Increases score per "by-click" value.
        """
        self.score += self.click

    def apply_profit(self):
        """Increases score by coffee per second.
        """
        if self.profit:
            self.score += self.profit / self.tickrate

    def save_game(self):
        """Uses the Repository class to generate data.csv and write game data into the file.

        Returns:
            file (SaveFile object): Current save file.
        """
        file = SaveFile(self.score, self.upgrades, self.cost, self.time_played)
        self.repository.save(file)
        return file

    def load_game(self):
        """Uses the Repository class to load data.csv and read game data from the file.
        """
        file = self.repository.load()
        self.score = file.score
        self.upgrades = file.upgrades
        self.cost = file.cost
        self.time_played = file.time_played
        self.calculate_profit()
