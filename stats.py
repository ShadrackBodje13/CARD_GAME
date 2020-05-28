import sys
import pygame
from pygame.locals import *

# Pour les stats du jeu mais je ne sais pas trop où les mettre
# la fonction stat ne prend rien en entrée,
# pour la dimension de l'ecran mais tu peux modifier en fonction de l'ecran chez toi Killian
screen = pygame.display.set_mode((1280, 910))


def stats():
    running = True  # selon ce que j'ai vu, running c'est pour executer la fonction ou le jeu jusqu'à ce que  l'utilisateur quitte la partie ou le jeu
    while running:  # tant que le jeu tourne
        screen.fill((192, 192, 192))  # ecran à redimensionner

        for event in pygame.event.get():  # si l'utilisateur quitte on quitte tout
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # running = false
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
