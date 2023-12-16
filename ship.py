from missile import Missile_S
from PIL import Image, ImageTk

class Ship:
    # Création du vaisseau, de sa position initiale et de son image
    def __init__ (self, x, y, window, canevas, width, height, img_path) : 
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.score = 0
        self.w = width / 2
        self.h = height - 70
        self.ship_pic = Image.open (img_path)
        self.ship_pic = self.ship_pic.resize ((100,100))
        self.pic = ImageTk.PhotoImage (self.ship_pic)
        self.player_item = self.canevas.create_image (self.w, self.h, image = self.pic)

    def ship_move (self, delta) :
        coord = self.canevas.coords (self.player_item)
        new_position = coord[0] + delta
        if 40 < new_position < 1490 : 
            self.canevas.move (self.player_item, delta, 0)
        
    def fire_shoot (self, window) :
        coord = self.canevas.coords(self.player_item)
        if len (coord) == 2 :
            shot = Missile_S (coord[0] + 7, coord[1] - 80, self.canevas, self)
            shot.bullet_ship (window)

    def get_score (self, score_label) :
        # Mettre à jour le texte du label avec la nouvelle valeur du score
        score_label.config (text = f"Score : {self.score}")

    def add_score (self, score_to_add, score_label) :
        # Fonction pour ajouter au score
        self.score += score_to_add
        self.get_score (score_label)

