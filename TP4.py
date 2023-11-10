from tkinter import Tk, Label, Button, Canvas, Text

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
Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'blue')
Canevas.pack(padx = 5, pady = 5)


# Affichage de la fenêtre
window.mainloop()