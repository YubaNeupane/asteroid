from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

import pygame


class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        ranAngle = random.uniform(20,50)
        ast1 = Asteroid(self.position.x, self.position.y,self.radius/2)
        ast2 = Asteroid(self.position.x, self.position.y,self.radius/2)
        ast1.velocity = 1.2 * pygame.Vector2(self.velocity.x, self.velocity.y).rotate(ranAngle)
        ast2.velocity = 1.2 * pygame.Vector2(self.velocity.x, self.velocity.y).rotate(-ranAngle)


