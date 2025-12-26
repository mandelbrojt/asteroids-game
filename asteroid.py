from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # small radius asteroid, just return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            smaller_one = pygame.math.Vector2.rotate(self.velocity, random_angle)
            smaller_two = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_one.velocity = smaller_one * 1.2
            asteroid_two.velocity = smaller_two * 1.2
