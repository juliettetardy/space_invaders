from tkinter import Tk, Label, Button, Canvas, Text, PhotoImage, NW, NE

# Création de la fenêtre du jeu
window = Tk()
window.title('Space Invaders Ju2 version')
score = 'score :'
#picture =  PhotoImage(file = "ciel_noir.gif")
label_start = Label(window, fg = 'navy', text = score)
label_start.grid()

button_quit = Button (window, text = 'Quit', fg = 'black', command = window.destroy)
button_quit.grid (row = 1, padx = 3, pady = 3)

bouton_start = Button(window, text="Start game", width=9)
bouton_start.grid (row = 2, sticky = NW, padx = 3, pady = 3)

bouton_stop = Button(window, text="Pause game", width=9)
bouton_stop.grid (row = 2, padx = 3, pady = 3)

button_new_game = Button (window, text = 'New game', fg ='black')
button_new_game.grid (row = 2, sticky = NE, padx = 3, pady = 3)

# Création d'un widget Canvas (zone graphique)
width_canvas = 1500
height_canvas = 700

Canevas = Canvas(window, width = width_canvas, height = height_canvas, bg = 'gray')
#item = Canevas.create_image (0, 0, anchor=NW, image = picture)
#print("Image de fond (item",item,")")
#Canevas.grid()

# ------------ Création des aliens ------------

# Couleurs des anneaux :
coul_for6 = ["red", "yellow", "blue", "green", "black", "purple"]
coul_for5 = ["pink", "orange", "brown", "white", "cornflowerblue"]

height_aliens = 30
for nmb_lines in range(1,4) :
    if nmb_lines%2 != 0 :
        # Coordonnées X,Y des anneaux :
        place_for6 = width_canvas/6 
        final_place_for6 = place_for6 - 20 - width_canvas/12
        coord_for6 = [[final_place_for6, height_aliens], [final_place_for6 + place_for6, height_aliens], [final_place_for6 + 2*place_for6, height_aliens], [final_place_for6 + 3*place_for6, height_aliens], [final_place_for6 + 4*place_for6, height_aliens], [final_place_for6 + 5*place_for6, height_aliens]]
        i = 0
        while i < 6 :
            x0, y0 = coord_for6[i][0], coord_for6[i][1]
            alien = Canevas.create_oval(x0, y0, x0+40, y0+40, width = 2, outline = 'black', fill = coul_for6[i])
            i += 1
    else : 
        # Coordonnées X,Y des anneaux :
        place_for5 = width_canvas/6
        final_place_for5 = place_for5 - 20 
        coord_for5 = [[final_place_for5, height_aliens], [final_place_for5 + place_for5, height_aliens], [final_place_for5 + 2*place_for5, height_aliens], [final_place_for5 + 3*place_for5, height_aliens], [final_place_for5 + 4*place_for5, height_aliens]]
        i = 0
        while i < 5 :
            x0, y0 = coord_for5[i][0], coord_for5[i][1]
            alien = Canevas.create_oval(x0, y0, x0+40, y0+40, width = 2, outline = 'black', fill = coul_for5[i])
            i += 1

    height_aliens += 80
    
# ------------ Création du vaisseau -----------

# Position initiale du vaisseau
PosX = width_canvas/2
PosY = 650

ship = Canevas.create_oval(PosX-10, PosY-10, PosX+10, PosY+10, width = 5, outline = 'black', fill = 'red')
#Canevas.focus_set()

def right_ship(evt):
    Canevas.move(ship, 10, 0)

def left_ship(evt):
    Canevas.move(ship, -10, 0)

Canevas.bind_all("<KeyPress-Right>", right_ship)
Canevas.bind_all("<KeyPress-Left>", left_ship)
Canevas.grid()

    
# Affichage de la fenêtre
window.mainloop()




