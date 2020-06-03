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

def cartes():
    card0 = randint(1, 60)
    sprite_card0 = 'cartes/carte' + str(card0) + '.png'
    card00 = pygame.image.load(sprite_card0).convert_alpha()
    card1 = randint(1, 60)
    sprite_card1 = 'cartes/carte' + str(card1) + '.png'
    card01 = pygame.image.load(sprite_card1).convert_alpha()
    card2 = randint(1, 60)
    sprite_card2 = 'cartes/carte' + str(card2) + '.png'
    card02 = pygame.image.load(sprite_card2).convert_alpha()
    card3 = randint(1, 60)
    sprite_card3 = 'cartes/carte' + str(card3) + '.png'
    card03 = pygame.image.load(sprite_card3).convert_alpha()
    card4 = randint(1, 60)
    sprite_card4 = 'cartes/carte' + str(card4) + '.png'
    card04 = pygame.image.load(sprite_card4).convert_alpha()
    card5 = randint(1, 60)
    sprite_card5 = 'cartes/carte' + str(card5) + '.png'
    card05 = pygame.image.load(sprite_card5).convert_alpha()
    card6 = randint(1, 60)
    sprite_card6 = 'cartes/carte' + str(card6) + '.png'
    card06 = pygame.image.load(sprite_card6).convert_alpha()
    
    #--------------------------------------------------------------------------
    #DECK JOUEUR 2
    
    card7 = randint(1, 60)
    sprite_card7 = 'cartes/carte' + str(card7) + '.png'
    card07 = pygame.image.load(sprite_card7).convert_alpha()
    card8 = randint(1, 60)
    sprite_card8 = 'cartes/carte' + str(card8) + '.png'
    card08 = pygame.image.load(sprite_card8).convert_alpha()
    card9 = randint(1, 60)
    sprite_card9 = 'cartes/carte' + str(card9) + '.png'
    card09 = pygame.image.load(sprite_card2).convert_alpha()
    card10 = randint(1, 60)
    sprite_card10 = 'cartes/carte' + str(card10) + '.png'
    card010 = pygame.image.load(sprite_card10).convert_alpha()
    card11 = randint(1, 60)
    sprite_card11 = 'cartes/carte' + str(card11) + '.png'
    card011 = pygame.image.load(sprite_card11).convert_alpha()
    card12 = randint(1, 60)
    sprite_card12 = 'cartes/carte' + str(card12) + '.png'
    card012 = pygame.image.load(sprite_card12).convert_alpha()
    card13 = randint(1, 60)
    sprite_card13 = 'cartes/carte' + str(card13) + '.png'
    card013 = pygame.image.load(sprite_card13).convert_alpha()
    
    #-------------------------------------------------------------------------
    
    #setting the life points
    points_de_vie = 2000
    #setting the enemy life points
    points_de_vie_2 = 2000
    #setting the font of texts
    font = pygame.font.SysFont("Arial", 50)
    #setting coordenates X and Y for cards
    x0 = 160
    y0 = 510
    y1 = 20
    x1 = 295
    x2 = 430
    x3 = 565
    x4 = 700
    x5 = 835
    x6 = 970
    xpixel = 100
    ypixel = 100
    #generating a null image in the battle field
    pixel = 'pixel.png'
    rien = 'rien.png'
    pixel2 = 'pixel2.png'
    #Boolean variable that determines if the card is in field
    dans_le_deck = False
    #Boolean variable that determines if the enemy card is in field
    dans_le_deck_2 = False
    #Damage variable
    degats = 0
    
    pixelload = False
    pixelload2 = False