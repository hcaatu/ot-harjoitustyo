import unittest
import pygame
from event_handler import EventHandler
from game_loop import GameLoop

class TestEventHandler(unittest.TestCase):
    def setUp(self):
        self.handler = EventHandler()
        self.ui = GameLoop().ui
        self.app = GameLoop().app

    def test_quit_event_is_classified_correctly(self):
        event = pygame.event.Event(256) # =quitting event
        self.handler.handle_events(event, self.ui, self.app)
        self.assertEqual(self.handler.running, False)

    def test_mouse_motion_is_classified_correctly(self):
        event = pygame.event.Event(1024, {'pos': (0, 0), 'rel': (0, 0), 'buttons': (0, 0, 0), 'touch': False, 'window': None}) # =mouse motion
        self.handler.handle_events(event, self.ui, self.app)
        self.assertEqual(self.handler.running, True)

    def test_mouse_button_down_is_classified_correctly(self):
        event = pygame.event.Event(1025, {'pos': (0, 0), 'button': 1, 'touch': False, 'window': None}) # =mouse button down
        self.handler.handle_events(event, self.ui, self.app)
        self.assertEqual(self.handler.running, True)

    def test_key_down_is_classified_correctly(self):
        event = pygame.event.Event(768, {'unicode': 'g', 'key': 103, 'mod': 0, 'scancode': 10, 'window': None}) # =pressing g on keyboard
        self.handler.handle_events(event, self.ui, self.app)
        self.assertEqual(self.handler.running, True)

        event = pygame.event.Event(768, {'unicode': '\x1b', 'key': 27, 'mod': 0, 'scancode': 41, 'window': None}) # pressing esc
        self.handler.handle_events(event, self.ui, self.app)
        self.assertEqual(self.handler.running, False)
