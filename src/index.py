import pygame
import os

class UI:
    def __init__(self):
        pygame.init()
        self.resolution = (640, 480)
        self.window = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.load_images()
        self.icon = self.images["matrix_logo"]
        self.update()

    def fill_screen(self, color):
        self.window.fill(color)

    def update(self):
        grey = (50, 50, 50)
        self.fill_screen(grey)
            
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.window.blit(self.icon, (320, 240))

            pygame.display.flip()
            self.clock.tick()

    def load_images(self):
        dirname = os.path.dirname(__file__)
        self.images = {}
        for name in ["matrix_logo"]:
            self.images[name] = pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            )

"""
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect =self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.image)
"""
        
UI()
#Block()