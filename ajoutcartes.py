# Fonction pour ajouter les cartes dans la main des joueurs


def add_card_to_hand(deck, joueur, delete=False):
    card_from_hand_to_deck = random.choice(deck.get_cards_from_deck())
    card_to_add = Card(card_from_hand_to_deck[1],  # au lieu de commencer à l'indice 0 [0]
                       card_from_hand_to_deck[2],
                       card_from_hand_to_deck[3],
                       card_from_hand_to_deck[4],
                       card_from_hand_to_deck[5],
                       card_from_hand_to_deck[6],
                       card_from_hand_to_deck[7],
                       card_from_hand_to_deck[8])
    joueur.hand.append(card_to_add)  # main du joueur (cart to hand)

    if delete:  # delete =False
        deck.del_card_from_deck(card_from_hand_to_deck)
