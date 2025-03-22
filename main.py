# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

GO = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def game_loop():
    while GO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop()

if __name__ == "__main__":
    main()
