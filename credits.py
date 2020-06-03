# Setup Python
import pygame, sys

#Création de la page
mainClock = pygame.time.Clock()
from random import randint
from pygame import *
pygame.init()
pygame.display.set_caption('RAP GAME')
screen = pygame.display.set_mode((1280, 720),0,32)

essaie = pygame.image.load('essaie.png')

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

def credits():
	
	running = True
	while True:
		screen.blit(essaie, (0,0))

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:	
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
					menu()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		mainClock.tick(60)