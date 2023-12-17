# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from PIL import Image, ImageTk
from missile import Missile_B
from math import cos, sin
from random import randint

class Boss :
    """
    Une classe qui permet de créer et afficher le boss
    Cette classe s'occupe de tous les éléments graphiques vis à vis du boss à afficher et de comment les afficher.

    Fonctions 
    ---------
        boss_move :
            Fonction qui gère le déplacement du boss sur le canevas
        boss_shot :
            Fonction qui permet au boss de tirer des missiles de manière aléatoire
        lost_life :
            Fonction qui gère la perte des vies à chaque fois que le boss en perd une
        
    """

    def __init__ (self, x, y, window, canevas, ship, image_path) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): 
            x : 
                Coordonnée en abscisse du boss sur l'écran
                type = int
            y : 
                Coordonnées en ordonnée du boss sur l'écran
                type = int
            window : 
                fenêtre associée au jeu ou apparaît le boss
                type = Tk
            canevas : 
                canevas du jeu sur lequel le boss va être placé
                type = Canvas
            ship : 
                ship représente le vaisseau du joueur/ le joueur
                type = int
            image_path : 
                image de l'alien
                type = str

        Sortie(s): None
        """
        self.x = x
        self.y = y
        self.speed = 10
        self.angle = 90
        self.dx = self.speed * cos (self.angle)
        self.dy = self.speed * sin (self.angle)

        self.window = window
        self.canevas = canevas
        self.ship = ship

        self.life_boss = 10
        self.var_life_boss = None

        self.boss_pic = Image.open (image_path)
        self.boss_pic = self.boss_pic.resize ((150, 150))
        self.pic = ImageTk.PhotoImage (self.boss_pic)
        self.boss_item = self.canevas.create_image (self.x + 20, self.y - 20, image = self.pic)

    def boss_move (self) :
        """ 
        Fonction qui gère le déplacement du boss sur le canevas
        Entrée(s): None
        Sortie(s): None

        """
        coord  = self.canevas.coords (self.boss_item)
        if len (coord) == 2 :
            if coord [0] + 20 >= 1510 or coord [0] - 20 <= 20 :  # collision avec les bords gauche et droite
                self.dx = - self.dx 
            if coord [1] + 20 >= 640 or coord [1] - 20 <= 0 :   # collision avec les bords haut et bas
                self.dy = - self.dy 

            # Le boss se déplace
            self.canevas.move (self.boss_item, self.dx, self.dy)

        # Exécute la fonction après un délai (pas immédiatement)
        self.window.after (20, self.boss_move)

    def boss_shot (self, back_img) :
        """ 
        Fonction qui permet au boss de tirer des missiles de manière aléatoire
        Entrée(s): 
            back_img : Image de fond du jeu ou se trouve les aliens
                type = int
        Sortie(s): None

        """
        can_shoot = randint (0, 150)
        if can_shoot == 150 :
            coord = self.canevas.coords (self.boss_item)
            if len (coord) == 2 :
                shot = Missile_B (coord [0] - 5, coord [1] + 80, self.window, self.canevas, self.ship, self.boss_item)
                shot.bullet_boss (back_img)
        
        # Exécute la fonction après un délai (pas immédiatement)
        self.window.after (30, lambda : self.boss_shot (back_img))

    def lost_life (self) :
        """ 
        Fonction qui gère la perte des vies à chaque fois que le boss en perd une
        Entrée(s): None
        Sortie(s): 
            0 : 
                Si c'est la dernière vie du boss
                type = int
            1 :
                Si le boss a perdu une vie
                type = int  

        """

        # Cas où le boss n'a plus qu'une vie
        if self.life_boss == 1 :
            self.life_boss -= 1
            if self.var_life_boss :
                self.var_life_boss.set (self.life_boss)
            return 1
        
        # Cas où le boss a encore des vies
        else :
            self.life_boss -= 1
            if self.var_life_boss :
                self.var_life_boss.set (self.life_boss)
            return 0