"""
Tardy Juliette et Curie Justine

TP4 CS-DEV - Réalisation d'un jeu type "Space Invaders" sous Tkinter
Utilisation de la programmation orientée objet.

Commencé le :
Fin du code le :

Il reste à faire :
- Mettre un menu Start game avec des règles --> ne pas commencer la partie directement
- Faire apparaître le nombre de vie restantes - Gérer les vies
- Faire apparaître le score (10 points pour un ennemi abattu, 
                            25 points si c'est un ennemi en capacité de tirer, 
                            150 points pour l'ennemi bonus)
- Gérer le cas où les aliens sont trop bas 
- Faire tirer les aliens de manière aléatoire
- Créer un ennemi bonus
- 
"""
 
from game import Game

go = Game()
window = go.get_window()
canevas = go.get_canevas()

go.create_widgets (window)
go.create_figures (window, canevas)

window.mainloop()