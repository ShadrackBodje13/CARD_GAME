# Je ne sais pas s'il faut le mettre sous forme de texte dans le jeu avec un print partie consigne ou l'appelé directement via ce fichier

PROJET: CARD GAME

Présentation

Projet inspiré du jeu “Castle Siege: Fantasy Card Game”. Le but est d’augmenter ses données tout en réduisant celles de l’adversaire afin de gagner la partie.


Fonctionnalités
   · cinq écrans: Difficulté: 2
     o menu principal avec accès aux autres écrans
      o écran de jeu avec possibilité de retour
       o écran de fin de partie
        o écran d’instructions avec possibilité de retour
        o écran d’options avec possibilité de retour

    · l’écran d’instructions devra présenter à l’utilisateur toutes les données nécessaires à la bonne utilisation du logiciel Difficulté: 1
    · modèle de données:
        o deux camps opposés, qui possèdent chacun: Difficulté: 2
         ▪ un index de joueur, premier ou deuxième
          ▪ des points de vie, par défaut 100, minimum 0, maximum 100
           ▪ des points de bouclier, par défaut 30, minimum 0, maximum 100
            ▪ 3 ressources différentes, qui possèdent chacune:
                · un fournisseur de ressource, minimum 1
                · un stock de ressource, par défaut 10, minimum 0
            ▪ une main de 7 cartes

        o une carte possède: Difficulté: 2
         ▪ un nom
          ▪ un type de ressource à dépenser
           ▪ un coût
            ▪ un type de donnée de camp à modifier(vie, bouclier, fournisseurs et stock)
            ▪ une valeur
            ▪ si elle affecte l’ennemi ou soi-même
            ▪ une probabilité d’apparition

    · Déroulement d’un tour:
        o le stock des ressources du joueur se voient incrémenté de 1 par fournisseur qu’il possède Difficulté: 1
        o si la main du joueur possède moins de 7 cartes, une carte est piochée en tenant compte des probabilités d’apparition des cartes. Difficulté: 2
        o le Joueur a deux possibilités:
            ▪ jouer une carte s'il peut payer le coût en ressource Difficulté: 2
            ▪ jeter une des cartes de sa main Difficulté: 1

        o fin du tour, début du tour adverse Difficulté: 1

    · fin d’une partie: Difficulté: 2
     o la partie se termine si un joueur à ses points de vie à 0 lors du début de son tour
      o le logiciel bascule alors sur l’écran de fin de partie, où diverses informations de la partie seront décrites

    · écran d’option:
        o il devra permettre à l’utilisateur de créer, consulter, modifier et supprimer(CRUD) toutes les cartes utilisées dans le logiciel Difficulté: 5
        o ces données devront être stockées dans un fichier afin de pouvoir les réutilisées même après fermeture du logiciel Difficulté: 3

    · deux modes de jeux devront être proposés:
        o mode deux joueurs en local Difficulté: 1
        o mode jouer contre une IA Difficulté: 5

Degré de difficulté total: 30 points
