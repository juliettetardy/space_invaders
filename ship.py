from missile import Missile

class Ship:

    def __init__(self, x, y, canevas): # Création du vaisseau et de sa position initiale
        self.canevas = canevas
        self.apparence = self.canevas.create_oval(x-10, y-10, x+10, y+10, width = 5, outline = 'black', fill = 'red')
        self.shoot = None

    def ship_move(self, delta):
        coord = self.canevas.coords(self.apparence)
        new_position = coord[2] + delta
        if 20 < new_position < 1495: 
            self.canevas.move(self.apparence, delta, 0)
        
    def fire_shoot(self, window):
        coord = self.canevas.coords(self.apparence)
        self.shoot = Missile(coord[0]+7, coord[1] - 10, self.canevas, self)
        self.shoot.bullet_move(window)


