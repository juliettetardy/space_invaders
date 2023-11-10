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
width_canvas = 480
height_canvas = 320 
Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'gray')
Canevas.pack(padx = 10, pady = 10)

# Coordonnées X,Y des 5 anneaux :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black"]
i = 0
while i < 5 :
     x0, y0 = coord[i][0], coord[i][1]
     Canevas.create_oval(x0, y0, x0+37, y0+37, width = 3, outline = 'black', fill = coul[i])
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




