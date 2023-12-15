class Missile :
    def __init__ (self, x, y, canevas, ship, score) :
        self.x = x
        self.y = y
        self.speed = - 15
        self.score = score 
        self.ship = ship
        self.canevas = canevas
        self.apparence = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'orange', fill = 'yellow')
    
    def bullet_move (self, window) :
        self.canevas.move (self.apparence, 0, self.speed)
        coord = self.canevas.coords (self.apparence)
        if len(coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord[3] < 0 :
                self.canevas.delete (self.apparence)
            for item in contacts :
                if item != self.apparence and item not in [1, self.apparence] :
                    self.canevas.delete(self.apparence)
                    self.canevas.delete(item)
                    self.score += 10
        window.after (30, lambda : self.bullet_move(window))

    def get_score (self) :
        return self.score