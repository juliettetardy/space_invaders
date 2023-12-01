    
class Islet :

    def __init__(self, x, y, side, canevas):
        self.x = x
        self.y = y
        self.side = side
        self.canevas = canevas

    def multiply_islet(self):
        for i in range (8):
            for j in range (3):
                self.canevas.create_rectangle(
                    self.x + (i)*self.side,
                    self.y + (j)*self.side, 
                    self.x + self.side + (i)*self.side, 
                    self.y + self.side + (j)*self.side ,
                    width = 1, outline = 'black', fill = 'gray' )
        
    
    