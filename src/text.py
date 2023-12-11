import pygame

class Text:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 24)
        self.italic = pygame.font.SysFont("Arial", 24, False, True)
        self.margin = 15
        self.leading = 26
        self.black = (0, 0, 0)

    def draw_textbox(self, window, pos):
        pass
