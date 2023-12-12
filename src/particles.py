import random
from image_loader import ImageLoader

class Particle:
    """This class is in charge of generating and calculating the positions of generated particles.
    """
    def __init__(self):
        """Constructor function for the class.
        """
        self.particles = ImageLoader().load_particles()
        self.timestep = 0
        self.a_value = 0
        self.direction = 0
        self.noise = 0
        self.img = self.choose_image()
        self.alpha = 255
        self.choose_parameters()

    def choose_parameters(self):
        """Chooses random parameters for a particle effect.
        """
        self.a_value = random.randrange(-15, 0)
        self.direction = random.choice((-1, 1))
        self.noise = random.randrange(0, 50)

    def choose_image(self):
        """Chooses an image at random for a particle.

        Returns:
            pygame.surface: Image
        """
        return random.choice(list(self.particles.values()))

    def calculate_pos(self, particle):
        """Calculates the current position for a particle when falling. 
        Trajectory is calculated by modeling a parabola.

        Args:
            particle (Particle object)

        Returns:
            tuple: Coordinates for the current position.
        """
        t = particle.timestep
        a = particle.a_value
        noise = particle.noise
        direction = particle.direction
        trajectory = t**2 + a * t
        center = (581, 278)
        return (center[0] + noise + 5*t * direction, center[1] + trajectory)

    def render_particle(self, particle, window):
        """Renders a particle given the parameters and adjusts them accordingly.

        Args:
            parameters (particle):
            window (pygame.display):
        """
        pos = self.calculate_pos(particle)
        window.blit(particle.img, pos)
