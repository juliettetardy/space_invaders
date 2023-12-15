# Importation des fichiers nécessaires au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Label, Frame, NW, W
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from islet import Islet

class Game :
    def __init__ (self) :
        self.window = Tk()
        self.window.title ('Space Invaders Ju2 version')

        self.score = 'Score :' 
        self.label_start = Label (self.window, fg = 'navy', text = "Score :")
        self.label_start.grid  (row = 1, sticky = W, padx = 3, pady = 3)
        self.life = 'Nombre de vie(s) :'
        self.label_life = Label (self.window, fg = 'navy', text = "Vie :")
        self.label_life.grid (row = 2, sticky = W, padx = 3, pady = 3)

        self.width_canvas = 1530
        self.height_canvas = 700
        self.Canevas = Canvas (self.window, width = self.width_canvas, height = self.height_canvas, bg = 'gray')

        self.back_pic = Image.open("images/milky_way.jpg")
        self.resized = self.back_pic.resize ((1530, 700))
        self.background = ImageTk.PhotoImage(self.resized)
    
    def get_window (self) :
        return self.window
    
    def get_canevas (self) :
        return self.Canevas

    def new_game (self) :
        self.Canevas.delete ('all') 
        self.create_widgets (self.window)
        self.create_figures (self.window, self.Canevas)
   
    def create_widgets (self, window) :
        button_quit = Button (window, text = 'Quit', fg = 'black', command = self.window.destroy)
        button_quit.grid (row = 2, padx = 3, pady = 3)

        #bouton_start = Button (window, text = "Start game", width = 9, command = lambda : self.start)
        #bouton_start.grid (row = 3, sticky = NW, padx = 3, pady = 3)

        button_new_game = Button (window, text = 'New game', fg ='black', command = self.new_game)
        button_new_game.grid (row = 1, padx = 3, pady = 3)

        # Ajout d'une image de fond 
        self.Canevas.create_image (0, 0, anchor = NW, image = self.background)
        self.Canevas.grid()

    def create_figures (self, window, Canevas) :
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

        # Création des missiles pour les aliens
        self.Canevas.bind_all("<KeyPress-Control_R>", lambda _: self.invaders.shoot_ship(window)) 

        # Création d'îlots protecteurs
        self.islet1 = Islet (100, 480, 25, Canevas)
        self.islet2 = Islet (1200, 480, 25, Canevas)
        self.islet3 = Islet (650, 480, 25, Canevas)

        self.islet1.multiply_islet()
        self.islet2.multiply_islet()
        self.islet3.multiply_islet()

# petit essai par ici
"""if __name__ == "__main__":
    app = Game()
    app.window.mainloop()"""









