# Importation des fichiers nécessaires au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Label, NW, W, IntVar
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from islet import Islet

class Game :
    def __init__ (self) :
        self.window = Tk()
        self.window.title ('Space Invaders Ju2 version')

        self.width_canvas = 1530
        self.height_canvas = 700
        self.Canevas = Canvas (self.window, width = self.width_canvas, height = self.height_canvas, bg = 'gray')

        self.score = IntVar()
        self.score.set (0)
        self.label_score = Label (self.window, fg = 'navy', textvariable = self.score)
        self.label_score.grid (row = 2, sticky = W, pady = 3)
        self.score_text = Label (self.window, fg = 'navy', text = "Score : ")
        self.score_text.grid (row = 1, sticky = W, pady = 3)

        self.life_nb = IntVar()
        self.life_nb.set (3)
        self.label_life = Label (self.window, fg = 'navy', textvariable = self.life_nb)
        self.label_life.grid (row = 4, sticky = W, padx = 3, pady = 3)
        self.life_text = Label (self.window, fg = 'navy', text = "Nombre de vie(s) : ")
        self.life_text.grid (row = 3, sticky = W, padx = 3, pady = 3)

        self.back_pic = Image.open ("images/milky_way.jpg")
        self.resized = self.back_pic.resize ((1530, 700))
        self.background = ImageTk.PhotoImage (self.resized)

    def get_window (self) :
        return self.window

    def new_game (self) :
        self.Canevas.delete ('all') 
        
        self.score.set (0)
        self.life_nb.set (3)

        img = self.create_widgets()
        self.create_figures (img)
   
    def create_widgets (self) :
        # Création du bouton pour détruire la fenêtre
        button_quit = Button (self.window, text = 'Quit', fg = 'navy', command = self.window.destroy)
        button_quit.grid (row = 4, padx = 3, pady = 3)

        #bouton_start = Button (window, text = "Start game", width = 9, command = lambda : self.start)
        #bouton_start.grid (row = 3, sticky = NW, padx = 3, pady = 3)

        # Crétion du bouton pour relancer une nouvelle partie
        button_new_game = Button (self.window, text = 'New game', fg ='navy', command = self.new_game)
        button_new_game.grid (row = 2, padx = 3, pady = 3)

        # Ajout d'une image de fond 
        item = self.Canevas.create_image (0, 0, anchor = NW, image = self.background)
        self.Canevas.grid()
        return item

    def create_figures (self, back_img = 1) :
        
        # Création d'îlots protecteurs
        islet1 = Islet (100, 480, 25, self.Canevas)
        islet2 = Islet (650, 480, 25, self.Canevas)
        islet3 = Islet (1200, 480, 25, self.Canevas)
        
        islet1.multiply_islet()
        islet2.multiply_islet()
        islet3.multiply_islet()

        # Création du vaisseau/joueur
        Player = Ship (765, 625, self.window, self.Canevas, self.width_canvas, self.height_canvas, "images/vaisseau_zinzins.png")
        self.Canevas.bind_all ("<KeyPress-Left>", lambda _: Player.ship_move (-15)) 
        self.Canevas.bind_all ("<KeyPress-Right>", lambda _: Player.ship_move (15)) 

        # Création des aliens
        invaders = Invaders (self.window, self.Canevas, Player, "images/alien_1.png")
        invaders.add_invaders()
        invaders.move_invaders()

        # Création d'un missile
        self.Canevas.bind_all ("<KeyPress-space>", lambda _: Player.fire_shoot (back_img)) 

        # Création des missiles pour les aliens
        invaders.shoot_ship (back_img)

        # Modification du score et de la vie
        Player.var_score = self.score
        Player.var_life = self.life_nb


