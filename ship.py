from missile import Missile_S
from PIL import Image, ImageTk

class Ship:
    # Création du vaisseau, de sa position initiale et de son image
    def __init__ (self, x, y, window, canevas, width, height, img_path) : 
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas

        self.life = 3
        self.var_life = None
        self.score = 0
        self.var_score = None

        self.w = width / 2
        self.h = height - 70
        self.ship_pic = Image.open (img_path)
        self.ship_pic = self.ship_pic.resize ((100,100))
        self.pic = ImageTk.PhotoImage (self.ship_pic)
        self.player_item = self.canevas.create_image (self.w, self.h, image = self.pic)

    def ship_move (self, delta) :
        coord = self.canevas.coords (self.player_item)
        if len (coord) == 2 :
            new_position = coord[0] + delta
            if 40 < new_position < 1490 : 
                self.canevas.move (self.player_item, delta, 0)
        
    def fire_shoot (self, back_img) :
        coord = self.canevas.coords (self.player_item)
        if len (coord) == 2 :
            shot = Missile_S (coord[0] + 7, coord[1] - 80, self.window, self.canevas, self)
            shot.bullet_ship (back_img)

    def get_score (self) :
        # Mettre à jour le texte du label avec la nouvelle valeur du score
        return self.score

    def add_score (self, score_to_add) :
        # Fonction pour ajouter au score
        self.score += score_to_add
        if self.var_score :
            self.var_score.set (self.score)

    def lost_life (self) :
        if self.life == 1 :
            self.life -= 1
            if self.var_life :
                self.var_life.set (self.life)
            return 1
        else :
            self.life -= 1
            if self.var_life :
                self.var_life.set (self.life)
            return 0