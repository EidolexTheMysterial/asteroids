import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)

            vect1 = self.velocity.rotate(rand_angle)
            vect2 = self.velocity.rotate(-rand_angle)

            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ast = Asteroid(self.position.x, self.position.y, new_rad)
            ast.velocity += vect1 * 1.2
            ast = Asteroid(self.position.x, self.position.y, new_rad)
            ast.velocity += vect2 * 1.2
