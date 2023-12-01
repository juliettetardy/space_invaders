from PIL import Image, ImageTk

class Ship:

    def __init__(self, x, y, canevas, window, width, height): # Création du vaisseau et de sa position initiale
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.apparence = self.canevas.create_oval(self.x-80, self.y-80, self.x+80, self.y+80, width = 5, outline = 'black', fill = 'red')
        
        self.w = width
        self.h = height
        self.position = [self.w / 2, self.h - 70]
        self.ship_pic = Image.open("images/vaisseau_zinzins.png")
        self.ship_pic = self.ship_pic.resize((130,130))
        self.ship_pic = ImageTk.PhotoImage(self.ship_pic)
        self.player_item = self.canevas.create_image(self.position[0], self.position[1], image = self.ship_pic)

    def ship_move(self, delta):
        coord = self.canevas.coords(self.apparence)
        new_position = coord[2] + delta
        if 20 < new_position < 1495: 
            left = self.canevas.move(self.apparence, delta, 0)
        
    def fire_shoot(self, window):
        coord = self.canevas.coords(self.apparence)
        self.shoot = Missile(coord[0]+7, coord[1] - 10, self.canevas, self)
        self.shoot.bullet_move(window)


