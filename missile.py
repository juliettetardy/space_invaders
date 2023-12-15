from random import randint

class Missile_A :
    def __init__ (self, x, y, canevas, ship) :
        self.x = x
        self.y = y
        self.speed_shot_s = - 15
        self.ship = ship
        self.canevas = canevas
        self.ship_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'brown')
        
    def bullet_ship (self, window) :
        self.canevas.move (self.ship_shot, 0, self.speed_shot_s)
        coord = self.canevas.coords (self.ship_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.ship_shot)
            for item in contacts :
                if item not in [1, self.ship_shot] :     # 1 correspond à l'image de fond
                    self.canevas.delete (self.ship_shot)
                    self.canevas.delete (item)
                    #self.ship.add_score(10)
        window.after (30, lambda : self.bullet_ship(window))

class Missile_I :
    def __init__ (self, x, y, canevas, ship) :
        self.x = x
        self.y = y
        self.speed_shot_i = 10
        self.ship = ship
        self.canevas = canevas
        self.invader_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'green')
    
    def bullet_invaders (self, window, invaders) :
        self.canevas.move (self.invader_shot, 0, self.speed_shot_i)
        coord = self.canevas.coords (self.invader_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.invader_shot)
            for item in contacts :
                dont_want = [1, self.invader_shot]             # 1 correspond à l'image de fond
                dont_want = dont_want + list (range(2,16))  # la liste de 2 à 15 correspond à tous les aliens
                if item not in dont_want :
                    self.canevas.delete (self.invader_shot)
                    self.canevas.delete (item)
                    #self.ship.add_score(-30)

        window.after (30, lambda : self.bullet_invaders (window, invaders))