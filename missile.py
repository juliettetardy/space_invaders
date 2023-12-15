class Missile :
    def __init__ (self, x, y, canevas, ship) :
        self.x = x
        self.y = y
        self.speed_shot_s = - 15
        self.speed_shot_i = 10
        self.ship = ship
        self.canevas = canevas
        self.ship_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'orange', fill = 'yellow')
        #self.invader_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'dark green', fill = 'green')
    
    def bullet_ship (self, window) :
        self.canevas.move (self.ship_shot, 0, self.speed_shot_s)
        coord = self.canevas.coords (self.ship_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.ship_shot)
            for item in contacts :
                if item != self.ship_shot and item not in [1, self.ship_shot] :
                    self.canevas.delete(self.ship_shot)
                    self.canevas.delete(item)
                    #self.ship.add_score(10)
        window.after (30, lambda : self.bullet_ship(window))

    def bullet_invaders (self, window, invaders) :
        self.canevas.move (self.invader_shot, 0, self.speed_shot_i)
        coord = self.canevas.coords (self.invader_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.invader_shot)
            for item in contacts :
                if item != self.invader_shot and item not in [1, self.invader_shot] :
                    invaders_list = list (range (2, 16))
                    if item not in invaders_list :
                        self.canevas.delete(self.invader_shot)
                        self.canevas.delete(item)
                        #self.ship.add_score(-30)
        window.after (30, lambda : self.bullet_invaders(window, invaders))
