# Setup Python
import pygame, sys

#Création de la page
mainClock = pygame.time.Clock()
from pygame import *
pygame.init()
pygame.display.set_caption('RAP GAME')
screen = pygame.display.set_mode((1280, 720),0,32)

background = pygame.image.load('assets/background.png')
background_1 = pygame.image.load('assets/background2.png')

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

def modedejeu():
	running = True
	while running:				
		
		screen.blit(background_1, (0,0))
		text('choix', font, (255, 255, 255), screen, 20, 20)
		
		mx, my = pygame.mouse.get_pos()
		
		button_5 = pygame.Rect(490, 300, 300, 75)
		button_6 = pygame.Rect(490, 400, 300, 75)	
		
		text('VS IA', font, (255, 255, 255), screen, 585, 320)
		text('LOCAL', font, (255, 255, 255), screen, 575, 420)

		pygame.draw.rect(screen, (0, 0, 0), button_5)
		pygame.draw.rect(screen, (0, 0, 0), button_6)
		
		if button_5.collidepoint((mx, my)):
			if click:
				jeu()
		if button_6.collidepoint((mx, my)):
			if click:
				localjeu()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
       
		pygame.display.update()
		mainClock.tick(60)


def jeu():
	running = True
	while running:
		screen.fill((0,0,0))
		text('JEU', font, (255, 255, 255), screen, 20, 20)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
       
		pygame.display.update()
		mainClock.tick(60)

def localjeu():
	running = True
	while running:
		screen.fill((0,0,0))
       
		text('localJEU', font, (255, 255, 255), screen, 20, 20)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
       
		pygame.display.update()
		mainClock.tick(60)

def instructions():
    running = True
    while running:
        screen.fill((0,0,0))
 
        text('INSTRUCTIONS', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        text('OPTIONS', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

def credits():
    running = True
    while running:
        screen.fill((0,0,0))
 
        text('CREDITS', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

menu()