# Setup Python
import pygame, sys

#Création de la page
mainClock = pygame.time.Clock()
from random import randint
from pygame import *
pygame.init()
pygame.display.set_caption('RAP GAME')
screen = pygame.display.set_mode((1280, 720),0,32)

plateau = pygame.image.load('plateau.png')

#son = pygame.mixer.Sound("assets/menu.wav")

font = pygame.font.SysFont(None, 50)

def text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) 

clock = pygame.time.Clock()

click = False 

#------------------------------------------------------------------------------

# Players will alternate turns.
def player_turns(total_turns):

    player_one = {
    "name": "Player 1",
    }
    player_two = {
    "name": "Player 2",
    }

    if total_turns % 2 == 0:
        total_turns += 1
        return player_one

    else:
        return player_two