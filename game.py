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
- Faire apparaître le nombre de vie restantes - Gérer les vies
- Faire apparaître le score (10 points pour un ennemi abattu, 
                            25 points si c'est un ennemi en capacité de tirer, 
                            150 points pour l'ennemi bonus)
- Gerer le cas où les aliens sont trop bas 
- Faire tirer les aliens de manières aléatoires
- Créer un ennemis bonus
- 
"""

# Importation des fichiers nécessaires au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Label, NW, NE
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from islet import Islet

class Game :
    def __init__ (self) :
        self.window = Tk()
        self.window.title('Space Invaders Ju2 version')
        self.score = 'Score :' 
        self.label_start = Label(self.window, fg = 'navy', text = "Score :")
        self.label_start.grid()
        self.back_pic = Image.open("images/milky_way.jpg")
        self.resized = self.back_pic.resize((1530, 700))
        self.background = ImageTk.PhotoImage(self.resized)
               
        self.width_canvas = 1530
        self.height_canvas = 700
        self.Canevas = Canvas(self.window, width = self.width_canvas, height = self.height_canvas, bg = 'gray')
        self.create_widgets(self.window)
        self.figure(self.window, self.Canevas)
        

 
    # Fonctions mise en marche et pause de l'animation
    def stop (self) : 
        # Cette fonction baisse le drapeau et arrête l'animation
        self.drapeau = False

    def start (self) :
        # Cette fonction lève le drapeau et lance l'animation
        if self.drapeau == False :       # Nécessaire pour ne pas lancer plusieurs fois l'animation
            self.drapeau = True
            Invaders.move_invaders()

    def create_widgets(self, window):

        button_quit = Button (window, text = 'Quit', fg = 'black', command = self.window.destroy)
        button_quit.grid(row = 1, padx = 3, pady = 3)

        bouton_start = Button(window, text = "Start game", width = 9, command = self.start)
        bouton_start.grid(row = 2, sticky = NW, padx = 3, pady = 3)

        bouton_stop = Button(window, text = "Pause game", width = 9, command = self.stop)
        bouton_stop.grid(row = 2, padx = 3, pady = 3)

        button_new_game = Button (window, text = 'New game', fg ='black')
        button_new_game.grid(row = 2, sticky = NE, padx = 3, pady = 3)


        # Ajout d'une image de fond 
        self.item = self.Canevas.create_image(0, 0, anchor = NW, image = self.background)
        print("Image de fond (item",self.item,")")
        self.Canevas.grid()

    def figure(self,window, Canevas):

        # Création des aliens
        self.invaders = Invaders(window, Canevas, "images/alien_1.png")
        self.invaders.add_invaders()
        self.invaders.move_invaders()

        # Création du vaisseau/joueur
        self.Player = Ship(765, 625, Canevas, window, self.width_canvas, self.height_canvas, "images/vaisseau_zinzins.png")

        self.Canevas.bind_all("<KeyPress-Left>", lambda _: self.Player.ship_move(-15)) 
        self.Canevas.bind_all("<KeyPress-Right>", lambda _: self.Player.ship_move(15)) 

        # Création d'un missile
        self.Canevas.bind_all("<KeyPress-space>", lambda _: self.Player.fire_shoot(window)) 


        # Création d'îlots protecteurs
        self.islet1 = Islet (100, 480, 25, Canevas)
        self.islet2 = Islet (1200, 480, 25, Canevas)
        self.islet3 = Islet (650, 480, 25, Canevas)

        self.islet1.multiply_islet()
        self.islet2.multiply_islet()
        self.islet3.multiply_islet()


if __name__ == "__main__":
    app = Game()
    app.window.mainloop()








