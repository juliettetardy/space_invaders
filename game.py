# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Label, NW, W, IntVar, Frame
from PIL import Image, ImageTk
from invaders import Invaders
from ship import Ship
from islet import Islet


class Game :
    """
    Une classe qui permet de jouer au jeu "Space Invaders _ Ju^2 Version".
    Cette classe s'occupe de tous les éléments graphiques à afficher et de comment les afficher.

    Fonctions 
    ---------
        start_game :
            Fonction qui démarre le jeu lorsque l'on est sur l'écran d"accueil.
        get_welcome_frame:
            Fonction qui affiche la frame du menu d'accueil.
        new_game :
            Fonction qui permet de jouer une nouvelle partie.
        create_widgets :
            Fonction qui rassemble et ajoute les widgets sur la frame du jeu principal.
        create_figures :
            Fonction qui créer les objets (aliens, vaisseau, missiles, îlots) à afficher.
        hide_score_and_life :
            Fonction qui permet de cacher le score et le nombre de vie restante.
        show_score_and_life :
            Fonction qui permet d'afficher le score et le nombre de vie restante.

    """
    def __init__ (self) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): None
        Sortie(s): None

        """

        # Création de la fenêtre et de son nom
        self.window = Tk()
        self.window.title ('Space Invaders Ju2 version')

        # Initialisation dimensions des canevas 
        self.width_canvas = 1530
        self.height_canvas = 700

        self.width_canvas_w = 1530
        self.height_canvas_w = 1000
    
        # Création de la frame "écran d'accueil"
        self.welcome_frame = Frame(self.window)
        self.Canevas_w = Canvas (self.welcome_frame, width = self.width_canvas_w, height = self.height_canvas_w, bg = 'gray')

        # Ajout d'un bouton pour démarrer le jeu
        button_start_game = Button (self.welcome_frame, text = 'Start game', fg ='navy', command = self.start_game)
        button_start_game.grid (row = 2, padx = 3, pady = 3)

        # Affichage de l'image de fond de la frame d'accueil
        self.back_pic_welc = Image.open ("images/front_page.jpg")
        self.resized_welc = self.back_pic_welc.resize ((1530, 1000))
        self.background_welc = ImageTk.PhotoImage (self.resized_welc)
        self.Canevas_w.create_image(0, 0, image = self.background_welc, anchor = NW)

        # Affichage du canevas associé à la frame d'accueil
        self.Canevas_w.grid()

        # Affichage la frame d'accueil 
        self.welcome_frame.grid()

        # création de la frame du jeu
        self.frame = Frame(self.window)
        self.Canevas = Canvas (self.frame, width = self.width_canvas, height = self.height_canvas, bg = 'gray')

        # Affichage de l'image de fond de la frame du jeu
        self.back_pic = Image.open ("images/milky_way.jpg")
        self.resized = self.back_pic.resize ((1530, 700))
        self.background = ImageTk.PhotoImage (self.resized)

        # Affichage de la frame
        self.frame.grid()

        # Initialisation de la variable score
        self.score = IntVar()
        self.score.set (0)

        # Affichage du score 
        self.label_score = Label (self.frame, fg = 'navy', textvariable = self.score)
        self.label_score.grid (row = 2, sticky = W, pady = 3)
        self.score_text = Label (self.frame, fg = 'navy', text = "Score : ")
        self.score_text.grid (row = 1, sticky = W, pady = 3)

         # Initialisation de la variable vie
        self.life_nb = IntVar()
        self.life_nb.set (3)
        
        # Affichage du nombre de vie restante
        self.label_life = Label (self.frame, fg = 'navy', textvariable = self.life_nb)
        self.label_life.grid (row = 4, sticky = W, padx = 3, pady = 3)
        self.life_text = Label (self.frame, fg = 'navy', text = "Remaining lives : ")
        self.life_text.grid (row = 3, sticky = W, padx = 3, pady = 3)

    def start_game(self):
        """ 
        Fonction qui démarre le jeu lorsque l'on est sur l'écran d"accueil 
        Entrée(s): None
        Sortie(s): None

        """
        # Suppression de la frame précédente (frame menu d'accueil)
        self.welcome_frame.grid_forget()

        # Affichage du score et des vies du joueur
        self.show_score_and_life()

        # Création et mise en route d'une partie
        self.new_game()
   

    def get_welcome_frame (self):
        """
        Fonction qui affiche la frame du menu d'accueil
        Entrée(s): None
        Sortie(s): 
            welcome_frame : Frame du menu d'accueil
                            type = frame    

        """
        # Masquage du score et des vies qui sont inutiles ici
        self.hide_score_and_life()

        # Affichage de la frame du menu d'accueil
        return self.welcome_frame

    def new_game (self) :
        """
        Fonction qui permet de jouer une nouvelle partie
        Entrée(s): None
        Sortie(s): None

        """
        # Supression de tout ce qu'il y a sur le Canevas
        self.Canevas.delete ('all') 

        # Réinitialisation des scores et du nombre de vie
        self.score.set (0)
        self.life_nb.set (3)

        # Remise à l'initiale des widgets et des figures sur le Canevas 
        img = self.create_widgets()
        self.create_figures (img)

    def create_widgets (self) :
        """
        Fonction qui rassemble et ajoute les widgets sur la frame du jeu principal
        Entrée(s): None
        Sortie(s): 
            background_img : Image de fond du jeu
                             type = int

        """
        # Création d'un bouton pour détruire la fenêtre
        button_quit = Button (self.frame, text = 'Quit', fg = 'navy', command = self.window.destroy)
        button_quit.grid (row = 4, padx = 3, pady = 3)

        # Crétion d'un bouton pour relancer une nouvelle partie
        button_new_game = Button (self.frame, text = 'New game', fg ='navy', command = self.new_game)
        button_new_game.grid (row = 2, padx = 3, pady = 3)

        # Ajout d'une image de fond 
        background_img = self.Canevas.create_image (0, 0, anchor = NW, image = self.background)
        self.Canevas.grid()
        return background_img

    def create_figures (self, back_img = 1) :
        """
        Fonction qui créer les objets (aliens, vaisseau, missiles, îlots) à afficher
        Entrée(s):
            back_img :  Background du jeu.
                        Si on ne veut pas afficher l'image de fond, il suffit de passer 0 en argument
                        type = int
        Sortie(s): None

        """
        # Création de 3 îlots protecteurs
        islet1 = Islet (100, 480, 25, self.Canevas)
        islet2 = Islet (650, 480, 25, self.Canevas)
        islet3 = Islet (1200, 480, 25, self.Canevas)
        islet1.multiply_islet()
        islet2.multiply_islet()
        islet3.multiply_islet()

        # Création du vaisseau/joueur
        Player = Ship(765, 625, self.frame, self.Canevas, self.width_canvas, self.height_canvas, "images/vaisseau_zinzins.png")

        # Gestion des déplacements du joueur en utilisant des touches du clavier
        self.Canevas.bind_all("<KeyPress-Left>", lambda _ : Player.ship_move (-15)) 
        self.Canevas.bind_all("<KeyPress-Right>", lambda _ : Player.ship_move (15)) 

        # Création des aliens et gestion de leur mouvements
        invaders = Invaders(self.frame, self.Canevas, Player, "images/alien_1.png")
        invaders.add_invaders()
        invaders.move_invaders()

        # Création d'un missile
        self.Canevas.bind_all("<KeyPress-space>", lambda _ : Player.fire_shoot(back_img)) 

        # Création des missiles pour les aliens
        invaders.shoot_ship(back_img)

        # Modification du score et de la vie
        Player.var_score = self.score
        Player.var_life = self.life_nb

    
    def hide_score_and_life(self):
        """
        Fonction qui permet de cacher le score et le nombre de vie restante.
        "grid_remove" est une fonction qui rend des éléments invisibles dans l'interface.
        Entrée(s): None
        Sortie(s): None

        """
        # Masquage du score 
        self.label_score.grid_remove() 
        self.score_text.grid_remove()

        # Masquage du nombre de vie
        self.label_life.grid_remove()
        self.life_text.grid_remove()

    def show_score_and_life(self):
        """
        Fonction qui permet d'afficher le score et le nombre de vie restante.
        "grid" permet d'afficher des éléments dans l'interface.
        Entrée(s): None
        Sortie(s): None

        """
        # Affichage du score
        self.label_score.grid()
        self.score_text.grid()

        # Affichage du nombre de vie
        self.label_life.grid()
        self.life_text.grid()


    



        

        


