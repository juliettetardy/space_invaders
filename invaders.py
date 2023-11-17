drapeau = False
class Invaders:

    def __init__(self, x, y, Canevas):
        self.x = x
        self. y = y
        self.speed = 5
        self.apparence = Canevas.create_oval(self.x, self.y, self.x + 40, self.y + 40, width = 2, outline = 'black', fill = 'green') 

    def invaders_move(self, Canevas, window):
        coord = Canevas.coords(self.apparence)
        if coord[2] >= 1500 or coord[0] <= 0:
            self.speed = -self.speed
        Canevas.move(self.apparence, self.speed, 0)

        window.after(20, lambda: self.invaders_move(Canevas, window)) 
        


    

