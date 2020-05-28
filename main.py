# Setup Python
import pygame, sys
from modedejeu import modedejeu



#Création de la page
mainClock = pygame.time.Clock()
from pygame import *
pygame.init()
pygame.display.set_caption('RAP GAME')
screen = pygame.display.set_mode((1280, 720),0,32)

background = pygame.image.load('background.png')
background_1 = pygame.image.load('background2.png')

#son = pygame.mixer.Sound("assets/menu.wav")

font = pygame.font.SysFont(None, 50)

def text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

click = False

def menu():
	while True:
		#!son.play()
		screen.blit(background, (0,0))
		text('menu', font, (255, 255, 255), screen, 20, 20)
		
		mx, my = pygame.mouse.get_pos()

		button_1 = pygame.Rect(490, 300, 300, 75)
		button_2 = pygame.Rect(490, 400, 300, 75)
		button_3 = pygame.Rect(490, 500, 300, 75)
		button_4 = pygame.Rect(490, 600, 300, 75)

		if button_1.collidepoint((mx, my)):
			if click:
				modedejeu()

		if button_2.collidepoint((mx, my)):
			if click:
				instructions()
		
		if button_3.collidepoint((mx, my)):
			if click:
				options()

		if button_4.collidepoint((mx, my)):
			if click:
				credits()

		pygame.draw.rect(screen, (0, 0, 0), button_1)
		pygame.draw.rect(screen, (0, 0, 0), button_2)
		pygame.draw.rect(screen, (0, 0, 0), button_3)
		pygame.draw.rect(screen, (0, 0, 0), button_4)

		text('JOUER', font, (255, 255, 255), screen, 575, 320)
		text('INSTRUCTIONS', font, (255, 255, 255), screen, 505, 420)
		text('OPTIONS', font, (255, 255, 255), screen, 555, 520)
		text('CREDITS', font, (255, 255, 255), screen, 555, 620)

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		mainClock.tick(60)

menu()