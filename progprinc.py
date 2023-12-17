"""
Tardy Juliette et Curie Justine

TP4 CS-DEV - Réalisation d'un jeu type "Space Invaders" sous Tkinter
Utilisation de la programmation orientée objet.

Commencé le : 10/11/2023
Dernière modification du code réalisée le : 17/12/2023

Il reste à faire :
- Faire apparaître le score (10 points pour un ennemi abattu, 
                            20 points si c'est un ennemi en capacité de tirer, 
                            150 points pour l'ennemi bonus)
- Créer un ennemi bonus
- Bonnes pratiques + commentaires fichier ship
- Bonnes pratiques + commentaires fichier missile (non terminé)
- Mettre des règles sur le menu start game
- Créer un READ ME
"""

# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from game import Game

# Récupération de la frame d'accueil
go = Game()
frame = go.get_welcome_frame()

# Bouclage de la frame 
frame.mainloop()