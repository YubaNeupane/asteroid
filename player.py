from circleshape import *
from shot import *

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED
import pygame

class Player (CircleShape):
    def __init__ (self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shootTimer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(),2)
    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation) 

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        
        if keys[pygame.K_w] :
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= forward * PLAYER_SPEED * dt
        
        self.shootTimer -= dt
        if keys[pygame.K_SPACE]:
            if self.shootTimer <= 0:
                self.shootTimer = 0.3
                self.shoot()
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

