class Ship:

    def __init__(self, x, y, Canevas): # Création du vaisseau et de sa position initiale
        self.x = x
        self.y = y
        self.Canevas = Canevas
        self.apparence = self.Canevas.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, width = 5, outline = 'black', fill = 'red')

    def ship_move(self, delta):
        coord = self.Canevas.coords(self.apparence)
        new_position = coord[2] + delta
        if 20 < new_position < 1495: 
            left = self.Canevas.move(self.apparence, delta, 0)




