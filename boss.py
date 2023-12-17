# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from PIL import Image, ImageTk
from missile import Missile_B
from math import cos, sin
from random import randint

class Boss :
    def __init__ (self, x, y, window, canevas, ship, img_path) :
        self.x = x
        self.y = y
        self.speed = 10
        self.angle = 0
        self.dx = self.speed * cos (self.angle)
        self.dy = self.speed * sin (self.angle)

        self.window = window
        self.canevas = canevas
        self.ship = ship

        self.life_boss = 10
        self.var_life_boss = None

        self.boss_pic = Image.open (img_path)
        self.boss_pic = self.boss_pic.resize ((100, 100))
        self.pic = ImageTk.PhotoImage (self.boss_pic)
        self.boss_item = self.canevas.create_image (self.x + 20, self.y + 20, image = self.pic)

    def boss_move (self) :
        coord  = self.canevas.coords (self.boss_item)
        if len (coord) == 2 :
            if coord [0] + 20 >= 1530 or coord [0] - 20 <= 0 :  # collision avec les bords gauche et droite
                self.speed = - self.speed 
            if coord [1] + 20 >= 700 or coord [1] - 20 <= 0 :   # collision avec les bords haut et bas
                self.speed = - self.speed 

    def boss_shot (self, back_img) :
        can_shoot = randint (0, 250)
        if can_shoot == 250 :
            coord = self.canevas.coords (self.boss_item)
            if len (coord) == 2 :
                shot = Missile_B (coord [0] - 5, coord [1] + 40, self.window, self.canevas, self.ship)
                shot.bullet_boss (back_img)
        
        self.window.after (30, lambda : self.boss_shot (back_img))

    def lost_life (self) :
        if self.life_boss == 1 :
            self.life_boss -= 1
            if self.var_life_boss :
                self.var_life_boss.set (self.life_boss)
            return 1
        else :
            self.life_boss -= 1
            if self.var_life_boss :
                self.var_life_boss.set (self.life_boss)
            return 0