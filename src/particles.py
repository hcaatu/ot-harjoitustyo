import random
from ui import AppUI

class Particle:
    def __init__(self):
        self.timer = 0
        self.ui = AppUI()
        self.particles = self.ui.particles
        self.particles_parameters = [0, 0, 0, 0]

    def choose_a_value(self):
        a_value = random.randrange(-25, 25)
        if a_value < 0:
            return (a_value, -1)
        return (a_value, 1)
    
    def choose_image(self):
        return random.choice(list(self.particles.values()))

    def calculate_pos(self, t, a_value, direction):
        trajectory = t**2 + a_value * t
        return (self.ui.center[0] + 10*t * direction, self.ui.center[1] + trajectory)

    def render_particles(self, t, a_value, direction, img):
        if self.timer:
            pos = self.calculate_pos(t, a_value, direction)
            self.ui.window.blit(img, pos)
            self.timer -= 1