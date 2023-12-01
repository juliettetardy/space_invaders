"""
Tardy Juliette et Curie Justine

TP4 CS-DEV - Réalisation d'un jeu type "Space Invaders" sous Tkinter
Utilisation de la programmation orientée objet.

Commencé le :
Fin du code le :

Il reste à faire :
- Mettre un menu start game avec des règles --> ne pas commencer la partie directement
- Faire fonctionner le bouton "recommencer"
- Faire fonctionner le bouton "pause"
- Faire apparaître le nombre de vie restantes - Gerer les vies
- Faire descendre les aliens
- Gerer le cas où les aliens sont trop bas 
- Faire tirer les aliens de manières aléatoires
- Creer un ennemis bonus
- Transformer les formes par des images
- 


"""

# Importation des fichiers nécessaires au fonctionnement du jeu
from tkinter import Tk, Canvas ,Button ,Label, PhotoImage, NW, NE
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from islet import Islet


# Fonctions mise en marche et pause de l'animation
def stop(drapeau) : 
    # Cette fonction baisse le drapeau et arrête l'animation
    drapeau = False

def start(drapeau) :
    # Cette fonction lève le drapeau et lance l'animation
    if drapeau == False :       # Nécessaire pour ne pas lancer plusieurs fois l'animation
        drapeau = True
        
        #Invader.invaders_move(Canevas, window





# Création de la fenêtre du jeu
window = Tk()
window.title('Space Invaders Ju2 version')
score = 'Score :'
label_start = Label(window, fg = 'navy', text = "Score :")
label_start.grid()

back_pic = Image.open("images/milky_way.jpg")
resized = back_pic.resize((1530, 700))
background = ImageTk.PhotoImage(resized)

button_quit = Button (window, text = 'Quit', fg = 'black', command = window.destroy)
button_quit.grid(row = 1, padx = 3, pady = 3)

bouton_start = Button(window, text="Start game", width=9, command = start)
bouton_start.grid(row = 2, sticky = NW, padx = 3, pady = 3)

bouton_stop = Button(window, text="Pause game", width=9, command = stop)
bouton_stop.grid(row = 2, padx = 3, pady = 3)

button_new_game = Button (window, text = 'New game', fg ='black')
button_new_game.grid(row = 2, sticky = NE, padx = 3, pady = 3)

# Création d'un widget Canvas (zone graphique)
width_canvas = 1530
height_canvas = 700
Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'gray')

# Ajout d'une image de fond
item = Canevas.create_image(0, 0, anchor=NW, image=background)
print("Image de fond (item",item,")")
Canevas.grid()

# Création des aliens
invaders = Invaders(window, Canevas, "images/alien_1.png")
invaders.add_invaders()
invaders.move_invaders()

# Création du vaisseau/joueur
Player = Ship(765, 625, Canevas, window, width_canvas, height_canvas, "images/vaisseau_zinzins.png")

Canevas.bind_all("<KeyPress-Left>", lambda _: Player.ship_move(-10)) 
Canevas.bind_all("<KeyPress-Right>", lambda _: Player.ship_move(10)) 

#création d'un missile
Canevas.bind_all("<KeyPress-space>", lambda _: Player.fire_shoot(window)) 


# Création d'îlots protecteurs

islet1 = Islet(100, 480, 25, Canevas)
islet2 = Islet(1200, 480, 25, Canevas)
islet3 = Islet(650, 480, 25, Canevas)

islet1.multiply_islet()
islet2.multiply_islet()
islet3.multiply_islet()


# Affichage de la fenêtre
window.mainloop()







