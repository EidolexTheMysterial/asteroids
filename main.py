# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

GO = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def game_loop():
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while GO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 100

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop()

if __name__ == "__main__":
    main()
