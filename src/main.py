import pygame as pg
from pygame.math import Vector2

class Game:
    def __init__(self): 
        pg.init()
        self.window = pg.display.set_mode((1280, 720))
        self.load_assets()
        self.start()
        self.start_screen = True
        self.clock = pg.time.Clock()
        self.vihu = self.assets[2]
        self.pos = (0, 0)
        

        self.update()

    def load_assets(self):   
        self.assets = []
        for name in ["play", "pause", "enemy"]:
            self.assets.append(pg.image.load(name + ".png"))

    def input(self): 
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 200<=x<=500 and 160<=y<=230 and self.start_screen:
                    self.level = 1
                    self.load_level()
                if 1170<=x<=1220 and 0<=y<=50 and not self.start_screen:
                    self.play = True
                    
                    

            if event.type == pg.QUIT:
                exit()

    def start(self):
        self.window.fill((255, 255, 255))
        font = pg.font.SysFont("Courier New", 30)
        select_level = font.render(("Select level:"), True, (0, 0, 0))
        level1 = font.render(("Level 1"), True, (255, 255, 255))
        self.window.blit(select_level, (100, 100))
        pg.draw.rect(self.window, (50, 50, 50), (200, 160, 300, 70), width=0, border_radius=20)
        self.window.blit(level1, (220, 180))
        self.wave_counter = 0
        self.play = False

    def draw_level(self):
        if self.level == 1:
            self.window.fill((144, 238, 144))
            pg.draw.rect(self.window, (151, 121, 97), (200, 0, 50, 400), width=0, border_radius=3)
            pg.draw.rect(self.window, (151, 121, 97), (200, 350, 250, 50), width=0, border_radius=3)
            pg.draw.rect(self.window, (151, 121, 97), (400, 400, 50, -250), width=0, border_radius=3)
            pg.draw.rect(self.window, (151, 121, 97), (400, 150, 300, 50), width=0, border_radius=3)
            pg.draw.rect(self.window, (151, 121, 97), (650, 150, 50, 400), width=0, border_radius=3)
            pg.draw.rect(self.window, (151, 121, 97), (650, 500, 900, 50), width=0, border_radius=3)
            
            

    def load_level(self):
        self.start_screen = False
        self.play = False
        if self.level == 1:
            self.path = [(200, -50), (200, 350), (400, 350), (400, 150), (650, 150), (650, 500), (1400, 500)]
            self.pos = self.path[0]
            self.level1 = True
            self.draw_level()
            self.draw_ui()
            #for i in self.level1_path:
            #    pygame.draw.rect(self.window, (0, 0, 0), (i[0], i[1], 10, 10))
            self.make_enemies(10, 1, self.wave_counter)

    def draw_ui(self):
        pg.draw.rect(self.window, (150, 150, 150), (1000, 0, 280, 720))
        pg.draw.rect(self.window, (100, 100, 100), (1000, 50, 280, 50))
        pg.draw.rect(self.window, (80, 80, 80), (1000, 0, 280, 50))
        pg.draw.rect(self.window, (50, 50, 50), (1170, 0, 50, 50), border_radius=10)
        pg.draw.rect(self.window, (50, 50, 50), (1225, 0, 50, 50), border_radius=10)
        font = pg.font.SysFont("Courier New", 30)
        towers = font.render(("Towers"), True, (255, 255, 255))
        wave = font.render((f"Wave {self.wave_counter}"), True, (255, 255, 255))
        self.window.blit(towers, (1082, 60))
        self.window.blit(wave, (1010, 10))
        self.window.blit(self.assets[0], (1185, 10))
        self.window.blit(self.assets[1], (1240, 10))

    def make_enemies(self, count:int, speed:float, strength:float):
        for i in range(count):
            self.image = self.assets[2].convert_alpha()
            self.vel = Vector2(0, 0)
            self.pos = Vector2(self.pos)
            self.count = count
            self.speed = speed
            self.strength = strength
            self.path_index = 1
            self.target = self.path[self.path_index]
            self.target_radius = 50
            self.rect = self.image.get_rect(center=self.pos)

    def move_enemies(self):
        heading = self.target - self.pos
        dist = heading.length()
        heading.normalize_ip()

        if dist <= 2:
            self.path_index = (self.path_index + 1) % len(self.path)
            self.target = self.path[self.path_index]

        self.vel = heading * self.speed

        self.pos += self.vel
        self.rect.center = self.pos
        self.draw_level()
        self.window.blit(self.image, self.pos)
        self.draw_ui()
    


                
    def draw_screen(self):
        if self.play:
            self.move_enemies()

        pg.display.flip()
        self.clock.tick(600)

                

    def update(self):
        while True:
            self.input()
            self.draw_screen()
            

if __name__ == "__main__":
    Game()

