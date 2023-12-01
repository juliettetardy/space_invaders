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
def stop() : 
    # Cette fonction baisse le drapeau et arrête l'animation
    global drapeau
    drapeau = False

def start() :
    # Cette fonction lève le drapeau et lance l'animation
    global drapeau
    if drapeau == False :       # Nécessaire pour ne pas lancer plusieurs fois l'animation
        drapeau = True
        Invader1.invaders_move()



# Création de la fenêtre du jeu
window = Tk()
window.title('Space Invaders Ju2 version')
score = 'Score :'
label_start = Label(window, fg = 'navy', text = score)
label_start.grid()

my_pic = Image.open("images/milky_way.jpg")
resized = my_pic.resize((1500, 700))
new_pic = ImageTk.PhotoImage(resized)

button_quit = Button (window, text = 'Quit', fg = 'black', command = window.destroy)
button_quit.grid(row = 1, padx = 3, pady = 3)

bouton_start = Button(window, text="Start game", width=9, command = start)
bouton_start.grid(row = 2, sticky = NW, padx = 3, pady = 3)

bouton_stop = Button(window, text="Pause game", width=9, command = stop)
bouton_stop.grid(row = 2, padx = 3, pady = 3)

button_new_game = Button (window, text = 'New game', fg ='black')
button_new_game.grid(row = 2, sticky = NE, padx = 3, pady = 3)

# Création d'un widget Canvas (zone graphique)
width_canvas = 1500
height_canvas = 700
Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'gray')

# Ajout d'une image de fond
item = Canevas.create_image(0, 0, anchor=NW, image=new_pic)
print("Image de fond (item",item,")")
Canevas.grid()

# Création d'un alien 
Invader1 = Invaders(750, 25, Canevas)
Invader1.invaders_move(Canevas, window)

#Création du vaisseau/ joueur
Player = Ship(750 ,625, Canevas)

Canevas.bind_all("<KeyPress-Left>", lambda _: Player.ship_move(-10)) 
Canevas.bind_all("<KeyPress-Right>", lambda _: Player.ship_move(10)) 

#création d'un missile
Canevas.bind_all("<KeyPress-space>", lambda _: Player.fire_shoot(window)) 


# Création d'îlots protecteurs

islet1 = Islet(100, 520, 25, Canevas)
islet2 = Islet(1200, 520, 25, Canevas)
islet3 = Islet(650, 520, 25, Canevas)

islet1.multiply_islet()
islet2.multiply_islet()
islet3.multiply_islet()

# Affichage de la fenêtre
window.mainloop()







