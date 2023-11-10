from tkinter import Tk, Label, Button, Canvas, Text

# def Alien() :

# Création de la fenêtre du jeu
window = Tk()

label_start = Label(window, text = 'Space Invaders', fg = 'navy')
label_start.pack()

button_quit = Button (window, text = 'QUIT', fg = 'black', command = window.destroy)
button_quit.pack()

button_new_game = Button (window, text = 'New game', fg ='black')
button_new_game.pack()

lives = Text(window, )

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

# Affichage de la fenêtre
window.mainloop()