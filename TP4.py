from tkinter import Tk, Label, Button, Canvas, Text

# def Alien() :

# Création de la fenêtre du jeu
window = Tk()
window.title('Space Invaders Ju2 version')
score = 'score :'

label_start = Label(window, fg = 'navy', text = score)
label_start.pack()

button_quit = Button (window, text = 'QUIT', fg = 'black', command = window.destroy)
button_quit.pack()

button_new_game = Button (window, text = 'New game', fg ='black')
button_new_game.pack()

# Création d'un widget Canvas (zone graphique)
width_canvas = 1500
height_canvas = 700
Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'gray')
Canevas.pack(padx = 10, pady = 10)

# ------------ Création des aliens ------------
# Coordonnées X,Y des 5 anneaux :
place = width_canvas/6 
final_place = place - 20 - 125
coord = [[final_place,30], [final_place + place,30], [final_place + 2*place,30], [final_place + 3*place,30], [final_place + 4*place, 30], [final_place + 5*place,30]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black", "purple"]
i = 0
while i < 6 :
     x0, y0 = coord[i][0], coord[i][1]
     Canevas.create_oval(x0, y0, x0+40, y0+40, width = 2, outline = 'black', fill = coul[i])
     i = i + 1

# ------------ Création du vaisseau ------------

# Position initiale du vaisseau
PosX = 250
PosY = 300

ship = Canevas.create_oval(PosX-10, PosY-10, PosX+10, PosY+10, width = 5, outline = 'black', fill = 'red')
Canevas.focus_set()

def right(evt):
    Canevas.move(ship, 5, 0)
 
def left(evt):
    Canevas.move(ship, -5, 0)
 
Canevas.bind_all("<KeyPress-Right>", right)
Canevas.bind_all("<KeyPress-Left>", left)
Canevas.pack(padx = 5, pady = 5)
    
# Affichage de la fenêtre
window.mainloop()