from circleshape import *
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__ (self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        print(dt)
        self.position += self.velocity * dt