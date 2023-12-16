import os
from pathlib import Path
from savefile import SaveFile

class Repository:
    """Repository class handles data writing, reading, and 
        making the .csv file into the correct format.
    """
    def __init__(self, file_path):
        self._path = file_path
        self.loaded_file = SaveFile(0, {}, {})

    def delete_all(self):
        Path(self._path).touch()
        os.remove(self._path)

    def save(self, save_file):
        self._write(save_file)
        return save_file

    def load(self):
        return self._read()

    def _ensure_file_exists(self):
        """Checks if a save file exists, and if not, initializes one in a correct format
        """
        if Path(self._path).exists():
            return
        Path(self._path).touch()

        with open(self._path, "w", encoding="utf-8") as file:
            data = '0\ncoffee_maker,0;aeropress,0;\ncoffee_maker,10;aeropress,100;'
            file.write(data)

    def _split_save_data(self, index, row):
        """Converts string into correct (dict) format

        Args:
            index (int): Iteration of the loop
            row (str): Single row of the data
        """
        row = row.replace("\n", "")
        if index == 0:
            self.loaded_file.score = float(row)

        elif index == 1:
            parts = row.split(";")
            for item in parts:
                if item == '':
                    break
                upgrade = item.split(",")
                self.loaded_file.upgrades[upgrade[0]] = int(upgrade[1])

        elif index == 2:
            parts = row.split(";")
            for item in parts:
                if item == '':
                    break
                cost = item.split(",")
                self.loaded_file.cost[cost[0]] = float(cost[1])

    def _read(self):
        """Reads data from the .csv file

        Returns:
            self.loaded_file: SaveFile object
        """
        self._ensure_file_exists()

        with open(self._path, encoding="utf-8") as file:
            index = 0
            for row in file:
                self._split_save_data(index, row)
                index += 1
        return self.loaded_file

    def _write(self, save_file: SaveFile):
        """Converts and writes data to the .csv file

        Args:
            save_file: SaveFile object
        """
        self._ensure_file_exists()

        with open(self._path, "w", encoding="utf-8") as file:
            score = str(save_file.score)
            uprgades = ""
            for key, item in save_file.upgrades.items():
                uprgades = uprgades + f"{key},{item};"
            cost = ""
            for key, item in save_file.cost.items():
                cost = cost + f"{key},{item};"

            data = score + "\n" + uprgades + "\n" + cost

            file.write(data)
