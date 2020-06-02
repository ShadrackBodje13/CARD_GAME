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

#  DECK JOUEUR 1

def jeu():
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
    
    #Printing the controls in console
    print ("""Appuyez sur 1 pour utiliser la premiere carte.
    Appuyez sur 2 pour utiliser la deuxieme carte.
    Aperte a tecla C para colocar a terceira carta da sua mao em campo.
    Aperte a tecla ALT para trocar a carta em campo.
    Aperte a tecla SPACE para atacar o oponente com a carta selecionada.
    """)
    
    pixelload = False
    pixelload2 = False
    tour = 1
    
    #-----------------------------------------------------------------------------------------
    #TOUR JOUEUR 1
    
    #Main loop:
    while True:
        while tour == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    #exit command
                    exit()
        
            #setting the card in battle field
            card_in_battle = pygame.image.load(pixel).convert_alpha()
            carta_do_oponente = pygame.image.load(pixel2).convert_alpha()
            #detecting pressed keys
            key = pygame.key.get_pressed()
            if key[K_1]:
                if dans_le_deck == False:
                    #first card in battle
                    pixel = sprite_card0
                    #generating another card
                    sprite_card0 = rien
                    card00 = pygame.image.load(sprite_card0).convert_alpha()
                    dans_le_deck = True
                    pixelload = True
        
            if key[K_2]:
                if dans_le_deck == False:
                    #second card in battle
                    pixel = sprite_card1
                    #generating another card
                    random = randint(1, 23)
                    sprite_card1 = rien
                    card01 = pygame.image.load(sprite_card1).convert_alpha()
                    dans_le_deck = True
                    pixelload = True
        
            if key[K_3]:
                if dans_le_deck == False:
                    #third card in battle
                    pixel = sprite_card2
                    #generating another card
                    random = randint(1, 23)
                    sprite_card2 = rien
                    card02 = pygame.image.load(sprite_card2).convert_alpha()
                    dans_le_deck = True
                    pixelload = True
        
            if key[K_4]:
                if dans_le_deck == False:
                    #third card in battle
                    pixel = sprite_card3
                    #generating another card
                    random = randint(1, 23)
                    sprite_card3 = rien
                    card03 = pygame.image.load(sprite_card3).convert_alpha()
                    dans_le_deck = True
                    pixelload = True
        
            if key[K_5]:
                if dans_le_deck == False:
                    #third card in battle
                    pixel = sprite_card4
                    #generating another card
                    random = randint(1, 23)
                    sprite_card4 = rien
                    card04 = pygame.image.load(sprite_card4).convert_alpha()
                    dans_le_deck = True
                    pixelload = True
        
            if key[K_6]:
                if dans_le_deck == False:
                    #third card in battle
                    pixel = sprite_card5
                    #generating another card
                    random = randint(1, 23)
                    sprite_card5 = rien
                    card05 = pygame.image.load(sprite_card5).convert_alpha()
                    dans_le_deck = True
                    pixelload = True
        
            if key[K_7]:
                if dans_le_deck == False:
                    #third card in battle
                    pixel = sprite_card6
                    #generating another card
                    random = randint(1, 23)
                    sprite_card6 = rien
                    card06 = pygame.image.load(sprite_card6).convert_alpha()
                    dans_le_deck = True
        
                
            if key[K_SPACE] and pixelload == True:
                #detecting the battle force
                battle_force=200
        
                #detecting the enemy battle force
                #if sprite_op=='cartes/carte1.png':
                    #c_battle_force=1000
        
                #detecting damage
                points_de_vie_2 = points_de_vie_2 - battle_force
                
                pixel = 'pixel.png'
                pixelload = False
                tour = 0
        
            if key[K_RETURN] and pixelload == True:
                #detecting the battle force
                battle_defense=50
        
                #detecting the enemy battle force
                #if sprite_op=='cartes/carte1.png':
                    #c_battle_force=1000
        
                #detecting damage
                points_de_vie  = points_de_vie + battle_defense
                
                pixel = 'pixel.png'
                pixelload = False
                tour = 0
            
            
            if key[K_TAB]:
                #changing the boolean variable to change the card in battle
                dans_le_deck = False
        
            #generating the life points text
            vida1 = font.render(str(points_de_vie), 1, (255, 0, 0))
            vida2 = font.render(str(points_de_vie_2), 1, (255, 0, 0))
        
            if points_de_vie <= 0 and points_de_vie_2 > 0:
                #detecting the game winner and displaying the lost mesage
                screen.blit(perdeu, (0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()
            if points_de_vie_2 <= 0 and points_de_vie > 0:
                #detecting the game winner and displaying the win mesage
                screen.blit(venceu, (0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()     
            #displaying the background
            screen.blit(plateau, (0, 0))
        
            screen.blit(card00, (x0, y0))
            screen.blit(card01, (x1, y0))
            screen.blit(card02, (x2, y0))
            screen.blit(card03, (x3, y0))
            screen.blit(card04, (x4, y0))
            screen.blit(card05, (x5, y0))
            screen.blit(card06, (x6, y0))
        
            screen.blit(card07, (x0, y1))
            screen.blit(card08, (x1, y1))
            screen.blit(card09, (x2, y1))
            screen.blit(card010, (x3, y1))
            screen.blit(card011, (x4, y1))
            screen.blit(card012, (x5, y1))
            screen.blit(card013, (x6, y1))
        
            #displaying the card in battle
            screen.blit(card_in_battle, (715, 265))
            #displaying the enemy card in battle
            screen.blit(carta_do_oponente, (430, 265))
            #displaying the life points
            screen.blit(vida1, (60, 360))
            #displaying the enemy life points
            screen.blit(vida2, (60, 300))
            #updating
            pygame.display.update()
            #Limiting the fps to 10
    
    #-----------------------------------------------------------------------------------------------
    
    #TOUR JOUEUR 2
    
        while tour == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    #exit command
                    exit()
        
            #setting the card in battle field
            carta_do_oponente = pygame.image.load(pixel2).convert_alpha()
            card_in_battle = pygame.image.load(pixel).convert_alpha()
            #detecting pressed keys
            key = pygame.key.get_pressed()
            if key[K_1]:
                if dans_le_deck_2 == False:
                    #first card in battle
                    pixel2 = sprite_card7
                    #generating another card
                    sprite_card7 = rien
                    card07 = pygame.image.load(sprite_card7).convert_alpha()
                    dans_le_deck_2 = True
                    pixelload2 = True
        
            if key[K_2]:
                if dans_le_deck_2 == False:
                    #second card in battle
                    pixel2 = sprite_card8
                    #generating another card
                    random = randint(1, 23)
                    sprite_card8 = rien
                    card08 = pygame.image.load(sprite_card8).convert_alpha()
                    dans_le_deck_2 = True
                    pixelload2 = True
        
            if key[K_3]:
                if dans_le_deck_2 == False:
                    #third card in battle
                    pixel2 = sprite_card9
                    #generating another card
                    random = randint(1, 23)
                    sprite_card9 = rien
                    card09 = pygame.image.load(sprite_card9).convert_alpha()
                    dans_le_deck_2 = True
                    pixelload2 = True
        
            if key[K_4]:
                if dans_le_deck_2 == False:
                    #third card in battle
                    pixel2 = sprite_card10
                    #generating another card
                    random = randint(1, 23)
                    sprite_card10 = rien
                    card010 = pygame.image.load(sprite_card10).convert_alpha()
                    dans_le_deck_2 = True
                    pixelload2 = True
        
            if key[K_5]:
                if dans_le_deck_2 == False:
                    #third card in battle
                    pixel2 = sprite_card11
                    #generating another card
                    random = randint(1, 23)
                    sprite_card11 = rien
                    card011 = pygame.image.load(sprite_card11).convert_alpha()
                    dans_le_deck_2 = True
                    pixelload2 = True
        
            if key[K_6]:
                if dans_le_deck_2 == False:
                    #third card in battle
                    pixel2 = sprite_card12
                    #generating another card
                    random = randint(1, 23)
                    sprite_card12 = rien
                    card012 = pygame.image.load(sprite_card12).convert_alpha()
                    dans_le_deck_12 = True
                    pixelload2 = True
        
            if key[K_7]:
                if dans_le_deck_2 == False:
                    #third card in battle
                    pixel2 = sprite_card13
                    #generating another card
                    random = randint(1, 23)
                    sprite_card13 = rien
                    card013 = pygame.image.load(sprite_card13).convert_alpha()
                    dans_le_deck_2 = True
                    pixelload2 = True
        
                
            if key[K_SPACE] and pixelload2 == True:
                #detecting the battle force
                battle_force2 = 200
        
                #detecting the enemy battle force
                #if sprite_op=='cartes/carte1.png':
                    #c_battle_force=1000
        
                #detecting damage
                points_de_vie = points_de_vie - battle_force2
                
                pixel2 = 'pixel2.png'
                pixelload2 = False
                tour = 1
    
            if key[K_RETURN] and pixelload2 == True:
                #detecting the battle force
                battle_defense_2=50
        
                #detecting the enemy battle force
                #if sprite_op=='cartes/carte1.png':
                    #c_battle_force=1000
        
                #detecting damage
                points_de_vie_2  = points_de_vie_2 + battle_defense_2
                
                pixel2 = 'pixel2.png'
                pixelload2 = False
                tour = 1
            
            if key[K_TAB]:
                #changing the boolean variable to change the card in battle
                dans_le_deck_2 = False
        
            #generating the life points text
            vida1 = font.render(str(points_de_vie), 1, (255, 0, 0))
            vida2 = font.render(str(points_de_vie_2), 1, (255, 0, 0))
        
            if points_de_vie <= 0 and points_de_vie_2 > 0:
                #detecting the game winner and displaying the lost mesage
                screen.blit(perdeu, (0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()
            if points_de_vie_2 <= 0 and points_de_vie > 0:
                #detecting the game winner and displaying the win mesage
                screen.blit(venceu, (0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()     
            #displaying the background
            screen.blit(plateau, (0, 0))
        
            screen.blit(card00, (x0, y0))
            screen.blit(card01, (x1, y0))
            screen.blit(card02, (x2, y0))
            screen.blit(card03, (x3, y0))
            screen.blit(card04, (x4, y0))
            screen.blit(card05, (x5, y0))
            screen.blit(card06, (x6, y0))
        
            screen.blit(card07, (x0, y1))
            screen.blit(card08, (x1, y1))
            screen.blit(card09, (x2, y1))
            screen.blit(card010, (x3, y1))
            screen.blit(card011, (x4, y1))
            screen.blit(card012, (x5, y1))
            screen.blit(card013, (x6, y1))
        
            #displaying the card in battle
            screen.blit(card_in_battle, (715, 265))
            #displaying the enemy card in battle
            screen.blit(carta_do_oponente, (430, 265))
            #displaying the life points
            screen.blit(vida1, (60, 360))
            #displaying the enemy life points
            screen.blit(vida2, (60, 300))
            #updating
            pygame.display.update()
            #Limiting the fps to 10