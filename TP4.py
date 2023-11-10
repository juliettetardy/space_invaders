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
# Coordonnées X,Y des anneaux :


# Couleurs des anneaux :
coul_for6 = ["red", "yellow", "blue", "green", "black", "purple"]
coul_for5 = ["pink", "orange", "brown", "white", "cornflowerblue"]


height_aliens = 30
for nmb_lines in range(1,3) :
    if nmb_lines%2 != 0 :
        place_for6 = width_canvas/6 
        final_place_for6 = place_for6 - 20 - width_canvas/12
        coord_for6 = [[final_place_for6, height_aliens], [final_place_for6 + place_for6, height_aliens], [final_place_for6 + 2*place_for6, height_aliens], [final_place_for6 + 3*place_for6, height_aliens], [final_place_for6 + 4*place_for6, height_aliens], [final_place_for6 + 5*place_for6, height_aliens]]
        i = 0
        while i < 6 :
            x0, y0 = coord_for6[i][0], coord_for6[i][1]
            Canevas.create_oval(x0, y0, x0+40, y0+40, width = 2, outline = 'black', fill = coul_for6[i])
            i += 1
    else : 
        place_for5 = width_canvas/5
        final_place_for5 = place_for5 - 20 - width_canvas/10
        coord_for5 = [[final_place_for5, height_aliens], [final_place_for5 + place_for5, height_aliens], [final_place_for5 + 2*place_for5, height_aliens], [final_place_for5 + 3*place_for5, height_aliens], [final_place_for5 + 4*place_for5, height_aliens]]
        i = 0
        while i < 5 :
            x0, y0 = coord_for5[i][0], coord_for5[i][1]
            Canevas.create_oval(x0, y0, x0+40, y0+40, width = 2, outline = 'black', fill = coul_for5[i])
            i += 1
    height_aliens += 80
    
    

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