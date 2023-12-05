import unittest
import os
import tempfile
from repository import SaveFile, Repository

class TestRepository(unittest.TestCase):
    # intialize with temporary files, so that tests work without dependencies
    def setUp(self):
        self.file = tempfile.NamedTemporaryFile(delete=False)
        self.file_path = self.file.name
        self.repository = Repository(self.file_path)
        self.repository.delete_all()

    def test_save_and_load(self):
        save_file = SaveFile(200, {'coffee_maker': 10, 'brewer': 5}, {'coffee_maker': 20, 'brewer': 50}, 500)

        saved_data = self.repository.save(save_file)

        self.assertEqual(saved_data.score, save_file.score)
        self.assertEqual(saved_data.upgrades, save_file.upgrades)
        self.assertEqual(saved_data.cost, save_file.cost)
        self.assertEqual(saved_data.time_played, save_file.time_played)

        loaded_data = self.repository.load()

        self.assertEqual(loaded_data.score, save_file.score)
        self.assertEqual(loaded_data.upgrades, save_file.upgrades)
        self.assertEqual(loaded_data.cost, save_file.cost)
        self.assertEqual(loaded_data.time_played, save_file.time_played)

    def test_ensure_file_exists(self):
        self.repository._ensure_file_exists()
        self.assertEqual(os.path.exists(self.file_path), True)
        
    def test_read_and_write(self):
        save_file = SaveFile(200, {'coffee_maker': 10, 'brewer': 5}, {'coffee_maker': 20, 'brewer': 50}, 500)
        
        self.repository._write(save_file)
        loaded_data = self.repository._read()

        self.assertEqual(loaded_data.score, save_file.score)
        self.assertEqual(loaded_data.upgrades, save_file.upgrades)
        self.assertEqual(loaded_data.cost, save_file.cost)
        self.assertEqual(loaded_data.time_played, save_file.time_played)
        
    