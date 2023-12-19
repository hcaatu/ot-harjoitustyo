class SaveFile:
    """Class SaveFile is used to read the save file into a correct format.
    """
    def __init__(self, score: int, upgrades: dict, cost :dict):
        self.score = score
        self.upgrades = upgrades
        self.cost = cost
