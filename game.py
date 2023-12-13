"""
Tardy Juliette et Curie Justine

TP4 CS-DEV - Réalisation d'un jeu type "Space Invaders" sous Tkinter
Utilisation de la programmation orientée objet.

Commencé le :
Fin du code le :

Il reste à faire :
- Mettre un menu Start game avec des règles --> ne pas commencer la partie directement
- Faire fonctionner le bouton "recommencer"
- Faire fonctionner le bouton "pause"
- Faire apparaître le nombre de vie restantes - Gérer les vies
- Faire apparaître le score (10 points pour un ennemi abattu, 
                            25 points si c'est un ennemi en capacité de tirer, 
                            150 points pour l'ennemi bonus)
- Gerer le cas où les aliens sont trop bas 
- Faire tirer les aliens de manière aléatoire
- Créer un ennemi bonus
- 
"""

# Importation des fichiers nécessaires au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Label, NW, NE
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from islet import Islet
from missile import Missile

# Fonctions mise en marche et pause de l'animation
def stop (drapeau, canevas) : 
    # Cette fonction baisse le drapeau et arrête l'animation
    drapeau = False

def start (drapeau) :
    # Cette fonction lève le drapeau et lance l'animation
    if drapeau == False :       # Nécessaire pour ne pas lancer plusieurs fois l'animation
        drapeau = True
        Invaders.move_invaders()

# Création fenêtre avant que le jeu ne démarre 
window = Tk()
window.title('Space Invaders Ju2 version')
score = 'Score :' 
label_start = Label(window, fg = 'navy', text = "Score :")

def update_score_label(self):
    score = Missile.get_score(self)
    label_start = Label(window, fg = 'navy')
    label_start.config(text = "Score : " + str(score))
    window.after(100, update_score_label)

label_start.grid()

back_pic = Image.open("images/milky_way.jpg")
resized = back_pic.resize((1530, 700))
background = ImageTk.PhotoImage(resized)

button_quit = Button (window, text = 'Quit', fg = 'black', command = window.destroy)
button_quit.grid(row = 1, padx = 3, pady = 3)

bouton_start = Button(window, text = "Start game", width = 9, command = start)
bouton_start.grid(row = 2, sticky = NW, padx = 3, pady = 3)

bouton_stop = Button(window, text = "Pause game", width = 9, command = stop)
bouton_stop.grid(row = 2, padx = 3, pady = 3)

button_new_game = Button (window, text = 'New game', fg ='black')
button_new_game.grid(row = 2, sticky = NE, padx = 3, pady = 3)

# Création d'un widget Canvas (zone graphique)
width_canvas = 1530
height_canvas = 700
Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'gray')

# Ajout d'une image de fond 
item = Canevas.create_image(0, 0, anchor = NW, image = background)
print("Image de fond (item",item,")")
Canevas.grid()

# Création des aliens
invaders = Invaders(window, Canevas, "images/alien_1.png")
invaders.add_invaders()
invaders.move_invaders()

# Création du vaisseau/joueur
Player = Ship(765, 625, Canevas, window, width_canvas, height_canvas, "images/vaisseau_zinzins.png")

Canevas.bind_all("<KeyPress-Left>", lambda _: Player.ship_move(-15)) 
Canevas.bind_all("<KeyPress-Right>", lambda _: Player.ship_move(15)) 

# Création d'un missile
Canevas.bind_all("<KeyPress-space>", lambda _: Player.fire_shoot(window)) 

# Création d'îlots protecteurs
islet1 = Islet (100, 480, 25, Canevas)
islet2 = Islet (1200, 480, 25, Canevas)
islet3 = Islet (650, 480, 25, Canevas)

islet1.multiply_islet()
islet2.multiply_islet()
islet3.multiply_islet()

#update_score_label()

# Affichage de la fenêtre
window.mainloop()




