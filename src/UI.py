import pygame

class UI:
    def __init__(self):
        pygame.init()
        self.resolution = (640, 480)
        
        self.window = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
      # self.load_images()
        self.icon = pygame.Surface([100, 100])
        self.icon.fill((255, 0, 0))
        self.center = (self.resolution[0]/2 - self.icon.get_width()/2, self.resolution[1]/2 - self.icon.get_height()/2)
        self.score = 0
        self.update()

    def fill_screen(self, color):
        self.window.fill(color)

    def update(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.MOUSEBUTTONDOWN:
                        if event.pos[0] > 270 and event.pos[1] > 190:
                            if event.pos[0] < 370 and event.pos[1] < 290:
                                self.score += 1
                    if event.key == pygame.K_a:
                        self.score += 1

            grey = (200, 200, 200)
            self.fill_screen(grey)

            self.window.blit(self.icon, (self.center))

            font = pygame.font.SysFont("Arial", 24)
            counter = font.render(f"Score: {str(self.score)}", True, (255, 0, 0))
            self.window.blit(counter, (0, 0))

            pygame.display.flip()
            self.clock.tick()

"""
    def load_images(self):
        dirname = os.path.dirname(__file__)
        self.images = {}
        for name in ["logo"]:
            self.images[name] = pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            )
"""

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