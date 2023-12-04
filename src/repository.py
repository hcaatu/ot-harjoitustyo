import os
from pathlib import Path

dirname = os.path.dirname(__file__)

class SaveFile:
    def __init__(self, score: int, upgrades: dict, cost :dict, time_played: int):
        self.score = score
        self.upgrades = upgrades
        self.cost = cost
        self.time_played = time_played

class Repository:
    def __init__(self, file_path):
        self._path = file_path

    def find_all(self):
        return self._read()

    def save(self, save_file):
        self._write(save_file)
        return save_file

    def load(self):
        return self._read()

    def _ensure_file_exists(self):
        if Path(self._path).exists():
            return
        Path(self._path).touch()

        # Initialize save data structure, if doesn't exist

        with open(self._path, "w", encoding="utf-8") as file:
            data = '0\ncoffee_maker,0;\ncoffee_maker,10;\n0'
            file.write(data)

    def _read(self):
        loaded_file = SaveFile(0, {}, {}, 0)
        self._ensure_file_exists()

        with open(self._path, encoding="utf-8") as file:
            index = 0
            for row in file:
                row = row.replace("\n", "")
                if index == 0:
                    loaded_file.score = float(row)

                elif index == 1:
                    parts = row.split(";")
                    for item in parts:
                        if item == '':
                            break
                        upgrade = item.split(",")
                        loaded_file.upgrades[upgrade[0]] = int(upgrade[1])

                elif index == 2:
                    parts = row.split(";")
                    for item in parts:
                        if item == '':
                            break
                        cost = item.split(",")
                        loaded_file.cost[cost[0]] = float(cost[1])

                elif index == 3:
                    loaded_file.time_played = float(row)

                index += 1
        return loaded_file

    def _write(self, save_file: SaveFile):
        self._ensure_file_exists()

        with open(self._path, "w", encoding="utf-8") as file:
            score = str(save_file.score)
            uprgades = ""
            for key, item in save_file.upgrades.items():
                uprgades = uprgades + f"{key},{item};"
            cost = ""
            for key, item in save_file.cost.items():
                cost = cost + f"{key},{item};"
            time_played = str(save_file.time_played)

            data = score + "\n" + uprgades + "\n" + cost + "\n" + time_played

            file.write(data)
