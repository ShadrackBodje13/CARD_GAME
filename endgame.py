# fonction de endgame lol
# peut etre on la mettra directement dans le mode de jeu
import sys
import pygame
from pygame.locals import *


def end_game():
    running = True
    while running:
        screen.fill((192, 192, 192))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
