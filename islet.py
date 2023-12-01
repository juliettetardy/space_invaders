    
class Islet :

    def __init__(self, x, y, side, canevas):
        self.x = x
        self.y = y
        self.side = side
        self.canevas = canevas

    def multiply_islet(self):
        for i in range (3):
            for j in range (6):
                self.canevas.create_rectangle(
                    self.x + (2*i + 1)*self.side,
                    self.y + (2*j + 1)*self.side, 
                    self.x+5 + (2*j + 1)*self.side, 
                    self.y+10 + (2*i + 1)*self.side)
        
    
    