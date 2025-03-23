# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def start_game():
    GO = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    dt = 0

    # main loop
    while GO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GO = False

        pygame.Surface.fill(screen, "black")

        updatable.update(dt)

        for ast in asteroids:
            for st in shots:
                if st.is_colliding(ast):
                    ast.kill()
                    st.kill()

            if ast.is_colliding(player):
                print("Game over!")
                GO = False

        for ast in drawable:
            ast.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 100

    print("-" * 100)
    print("[ Exiting Asteroids ]")

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.display.set_caption("Asteroids in Pygame")

    start_game()

if __name__ == "__main__":
    main()
