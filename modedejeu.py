# Setup Python
import pygame, sys
from jeu import *
from jeuia import *

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

def modedejeu():
	running = True
	while True:				
		
		screen.blit(background_1, (0,0))
		text('choix', font, (255, 255, 255), screen, 20, 20)

		key = pygame.key.get_pressed()
		if key[K_LEFT]:
			jeu()

		if key[K_RIGHT]:
			jeuia()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
       
		pygame.display.update()
		mainClock.tick(60)
