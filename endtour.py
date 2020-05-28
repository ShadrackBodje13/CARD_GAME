# Fonction de fin de tour


def end_turn():
    global tour  # tour sera une variable globale afin de pouvoir etre appelée partout
    print('Fin du tour')
    print('Tour ' + str(tour))
# N'oublie pas de modifier Killian avec ton ecran làbas j'ai mis des values pygames comme ça lol
    if tour % 2 == 0:  # au tour du joueur 1 de jouer
        rect_end_turn = pygame.Rect(10, 400, 1260, 100)
        pygame.draw.rect(screen, (0, 0, 0), rect_end_turn)
        text_tools.draw_text('Tour ' + str(tour + 1) + ' - C\'est au joueur 1 de jouer !',
                             font_title, (255, 255, 255), screen, 250, 420)
        pygame.display.flip()
        joueur1.add_action_to_stock()
        joueur1.add_gold_to_stock()
        joueur1.add_mana_to_stock()
    elif tour % 2 == 1:  # au tour du joueur deux de jouerur
        rect_end_turn = pygame.Rect(10, 400, 1260, 100)
        pygame.draw.rect(screen, (0, 0, 0), rect_end_turn)
        text_tools.draw_text('Tour ' + str(tour + 1) + ' - C\'est au joueur 2 de jouer !',
                             font_title, (255, 255, 255), screen, 250, 420)
        pygame.display.flip()

        joueur2.add_action_to_stock()
        joueur2.add_gold_to_stock()
        joueur2.add_mana_to_stock()
    tour += 1
    time.sleep(2)  # fonction python pour le temps time.sleep(t)
