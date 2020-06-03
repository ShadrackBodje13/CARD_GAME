# Setup Python
import pygame, sys

#Création de la page
mainClock = pygame.time.Clock()
from pygame import *
pygame.init()
pygame.display.set_caption('RAP GAME')
screen = pygame.display.set_mode((1280, 720),0,32)

background_1 = pygame.image.load('background2.png')

#son = pygame.mixer.Sound("assets/menu.wav")

font = pygame.font.SysFont(None, 50)

def text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect) 

click = False 

#------------------------------------------------------------------------------

def options(self, nom, img, valeur, cout, attaque, defense, position_x, position_y, height, width):
	self.cartes.append(carte)