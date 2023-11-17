from tkinter import Tk, Canvas ,Button ,Label, PhotoImage, NW, NE
from PIL import Image, ImageTk
from invaders import Invaders

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
resized = my_pic.resize((1500,700))
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
Invader1 = Invaders(370, 370, Canevas)
Invader1.invaders_move(Canevas, window)

# Affichage de la fenêtre
window.mainloop()







