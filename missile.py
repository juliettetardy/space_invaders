from ship import Ship

class Missile:

    def __init__(self, x, y, canevas):
        self.name = 'pewpew'
        if Missile.name == 'Player':
            self.direction = 1
        self.x = x
        self.y = y
        self.speed = 5
        self.canevas = canevas
        self.apparence = self.canevas.create_rectangle(self.x, self.y, self.x+5, self.y+10, width = 5, outline = 'black', fill = 'yellow')
    
    def bullet(self, canevas, window): 
        self.canevas.move(self.apparence, 0, self.speed)
        window.after(60, lambda: self.bullet(canevas, window))
    
    
    



        

        

    
   