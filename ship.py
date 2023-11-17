class Ship:

    def __init__(self, x, y, canevas): # Création du vaisseau et de sa position initiale
        self.x = x
        self.y = y
        self.canevas = canevas
        self.apparence = self.canevas.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, width = 5, outline = 'black', fill = 'red')


    def ship_move(self, delta):
        coord = self.canevas.coords(self.apparence)
        new_position = coord[2] + delta
        if 20 < new_position < 1495: 
            left = self.canevas.move(self.apparence, delta, 0)




