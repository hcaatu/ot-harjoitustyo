import unittest
import pygame
from particles import Particle

class TestParticle(unittest.TestCase):
    def setUp(self):
        self.particle = Particle()
        self.particle._choose_parameters()

    def test_choose_parameters(self):
        self.assertTrue(self.particle.a_value in range(-15, 0))
        self.assertIn(self.particle.direction, (-1, 1))
        self.assertTrue(self.particle.noise in range(0, 50))

    def test_choose_image(self):
        image = self.particle._choose_image()
        self.assertEqual(type(image), pygame.Surface)
    
    def test_calculate_pos(self):
        # starting position
        pos = self.particle.calculate_pos(self.particle)
        self.assertEqual((581 + self.particle.noise, 278), pos)
        # later position
        self.particle.timestep = 10
        pos = self.particle.calculate_pos(self.particle)
        trajectory = self.particle.timestep**2 + self.particle.a_value * self.particle.timestep
        self.assertEqual((581 + self.particle.noise + 5*10*self.particle.direction, 278 + trajectory), pos)
