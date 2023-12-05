import unittest
from app import App
from repository import Repository

class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self.app = App()
        
    