from tkinter import Tk, Canvas ,Button ,Label, PhotoImage, NW, NE
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from missile import Missile

# Fonctions mise en marche et pause de l'animation
def stop(drapeau) : 
    # Cette fonction baisse le drapeau et arrête l'animation
    drapeau = False

def start(drapeau) :
    # Cette fonction lève le drapeau et lance l'animation
    if drapeau == False :       # Nécessaire pour ne pas lancer plusieurs fois l'animation
        drapeau = True
        
        Invader.invaders_move()

def canvas_limit(invaders) :
    print("coucou")
    if invaders[5].x == 1500 and invaders[-1].x == 1500 :
        print("1")
        for bad_guy in invaders : 
            bad_guy.invaders_move(Canevas, window)
    elif invaders[0].x == 0 and invaders[11].x == 0 :
        print("2")
        for bad_guy in invaders : 
            bad_guy.invaders_move(Canevas, window)
    else :
        print("3")
        for bad_guy in invaders : 
            bad_guy.invaders_move(Canevas, window)

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

# Création des aliens
bad_guys = []
height_aliens = 30
for nmb_lines in range(1,4) :
    if nmb_lines%2 != 0 :
        # Coordonnées X,Y des aliens :
        place_for6 = width_canvas/6 
        final_place_for6 = place_for6 - 20 - width_canvas/12
        coord_for6 = [[final_place_for6, height_aliens], [final_place_for6 + place_for6, height_aliens], [final_place_for6 + 2*place_for6, height_aliens], [final_place_for6 + 3*place_for6, height_aliens], [final_place_for6 + 4*place_for6, height_aliens], [final_place_for6 + 5*place_for6, height_aliens]]
        i = 0
        while i < 6 :
            x0, y0 = coord_for6[i][0], coord_for6[i][1]
            Invader = Invaders(x0, y0, Canevas)
            bad_guys.append(Invader)
            i += 1
    else : 
        # Coordonnées X,Y des aliens :
        place_for5 = width_canvas/6
        final_place_for5 = place_for5 - 20 
        coord_for5 = [[final_place_for5, height_aliens], [final_place_for5 + place_for5, height_aliens], [final_place_for5 + 2*place_for5, height_aliens], [final_place_for5 + 3*place_for5, height_aliens], [final_place_for5 + 4*place_for5, height_aliens]]
        i = 0
        while i < 5 :
            x0, y0 = coord_for5[i][0], coord_for5[i][1]
            Invader = Invaders(x0, y0, Canevas)
            bad_guys.append(Invader)
            i += 1
    height_aliens += 80

window.after(20, lambda: canvas_limit(bad_guys))
#bad_guys[0].invaders_move(Canevas, window)

# Création du vaisseau/ joueur
Player = Ship(750 ,625, Canevas)

Canevas.bind_all("<KeyPress-Left>", lambda _: Player.ship_move(-10)) 
Canevas.bind_all("<KeyPress-Right>", lambda _: Player.ship_move(10)) 

#création d'un missile
Coord = Ship.canevas.coord(Ship.apparence)
Missile = Missile(Coord, Canevas, window )
Canevas.bind_all("<KeyPress-Space>", lambda _: Player.missile(10)) 

# Affichage de la fenêtre
window.mainloop()







