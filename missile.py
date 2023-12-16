#from game import Game

class Missile_S :
    def __init__ (self, x, y, window, canevas, ship) :
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.speed_shot_s = - 15
        self.ship = ship
        self.ship_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'brown')
        
    def bullet_ship (self, back_img) :
        self.canevas.move (self.ship_shot, 0, self.speed_shot_s)
        coord = self.canevas.coords (self.ship_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.ship_shot)
            for item in contacts :
                if item not in [back_img, self.ship_shot] :     # 1 correspond à l'image de fond
                    self.canevas.delete (self.ship_shot)
                    self.canevas.delete (item)
                    #self.ship.add_score (10, Game().update_score())
        self.window.after (30, lambda : self.bullet_ship (back_img))

class Missile_I :
    def __init__ (self, x, y, window, canevas, ship) :
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.speed_shot_i = 10
        self.ship = ship
        self.invader_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'green')
    
    def bullet_invaders (self, back_img, invaders) :
        self.canevas.move (self.invader_shot, 0, self.speed_shot_i)
        coord = self.canevas.coords (self.invader_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.invader_shot)
            for item in contacts :
                dont_want = [back_img, self.invader_shot]      # 1 correspond à l'image de fond
                invaders = list (range(2,16))          # la liste de 2 à 15 correspond à tous les aliens
                dont_want = dont_want[:] + invaders[:]
                if item not in dont_want :
                    self.canevas.delete (self.invader_shot)
                    self.canevas.delete (item)
                    #self.ship.add_score (-30, Game().update_score())

        self.window.after (30, lambda : self.bullet_invaders (back_img, invaders))