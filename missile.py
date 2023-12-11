class Missile :
    def __init__ (self, x, y, canevas, ship) :
        self.x = x
        self.y = y
        self.speed = - 10
        self.ship = ship
        self.canevas = canevas
        self.apparence = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'orange', fill = 'yellow')
    
    def bullet_move(self,window) :
        self.canevas.move (self.apparence, 0, self.speed)
        contacts = self.canevas.find_overlapping (*self.canevas.coords(self.apparence))
        contacts = [item for item in contacts if item not in [1, self.apparence]]
        if contacts :
            to_delete = contacts + [self.apparence]
            for item in to_delete :
                self.canevas.delete (item)
        window.after (40, lambda : self.bullet_move(window))
