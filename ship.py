from missile import Missile
from PIL import Image, ImageTk

class Ship:

    def __init__(self, x, y, canevas, window, width, height, img_path): # Création du vaisseau et de sa position initiale
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        #self.apparence = self.canevas.create_oval(self.x-80, self.y-80, self.x+80, self.y+80, width = 5, outline = 'black', fill = 'red')
        
        self.w = width/2
        self.h = height -70
        self.ship_pic = Image.open(img_path)
        self.ship_pic = self.ship_pic.resize((130,130))
        self.pic = ImageTk.PhotoImage(self.ship_pic)
        self.player_item = self.canevas.create_image(self.w, self.h, image = self.pic)
    """
    def ship_move(self):
        print("2")
        if self.x >= 1530 or self.x <= 0 :
            self.speed = -self.speed

    """
    def ship_move(self, delta):
        print("1")
        coord = self.canevas.coords(self.player_item)
        new_position = coord[0] + delta
        if 20 < new_position < 1495: 
            left = self.canevas.move(self.apparence, delta, 0)
        
    def fire_shoot(self, window):
        coord = self.canevas.coords(self.apparence)
        self.shoot = Missile(coord[0]+7, coord[1] - 10, self.canevas, self)
        self.shoot.bullet_move(window)


