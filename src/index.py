import pygame
from random import randint

class UI:
    def __init__(self):
        pygame.init()
        self.resolution = (640, 480)
        self.window = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.main()

    def fill_screen(self, color):
        self.window.fill(color)

    def main(self):
        grey = (50, 50, 50)
        self.fill_screen(grey)
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

            pygame.display.flip()
            self.clock.tick()

UI()