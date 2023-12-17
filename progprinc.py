"""
Tardy Juliette et Curie Justine

TP4 CS-DEV - Réalisation d'un jeu type "Space Invaders" sous Tkinter
Utilisation de la programmation orientée objet.

Commencé le :
Fin du code le :

Il reste à faire :
- Mettre des règles sur le menu start game
- Redimensionner les fenêtres
- Faire apparaître le score (10 points pour un ennemi abattu, 
                            20 points si c'est un ennemi en capacité de tirer, 
                            150 points pour l'ennemi bonus)
- Créer un ennemi bonus
- 
"""
# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from game import Game

go = Game()
frame = go.get_welcome_frame()

frame.mainloop()