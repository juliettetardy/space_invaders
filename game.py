from tkinter import Tk, Canvas ,Button ,Label, PhotoImage

# Création de la fenêtre du jeu
window = Tk()
window.title('Space Invaders Ju2 version')
score = 'score :'
picture =  PhotoImage(file = "ciel_noir.gif")
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
item = Canevas.create_image(0,0,anchor=NW, image=picture)
print("Image de fond (item",item,")")
Canevas.pack()


# Affichage du Caneva
Canevas.pack()

# Affichage de la fenêtre
window.mainloop()






