import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import os


def writeText(screen,font,text,location,color=(255,255,255)):
    screen.blit(font.render(text,True,color),location)

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("ASTEROID")

    font_path = os.path.join('Quantico-Regular.ttf')
    font=pygame.font.Font(font_path,40)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        die = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                die = True
                player.die()
                if player.numberOfLives == 0:
                    print("Game over!")
                    sys.exit()
            if die:
                asteroid.kill()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split(player)
                    shot.kill()
        

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        

        writeText(screen,font, f"SCORE: {player.score:05d}", (100,20))
        writeText(screen,font, f"LIVES: {player.numberOfLives}", (SCREEN_WIDTH - 200,20))

        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
