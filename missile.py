# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import messagebox

class Missile_S :
    def __init__ (self, x, y, window, canevas, ship) :
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.speed_shot_s = - 15
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
                    self.ship.add_score (10)
        self.window.after (30, lambda : self.bullet_ship (back_img))

class Missile_I :
    def __init__ (self, x, y, window, canevas, ship) :
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.speed_shot_i = 10
        self.invader_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'green')
    
    def bullet_invaders (self, back_img, invaders) :
        self.canevas.move (self.invader_shot, 0, self.speed_shot_i)
        coord = self.canevas.coords (self.invader_shot)
        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :
                self.canevas.delete (self.invader_shot)
            else :
                for item in contacts :
                    dont_want = [back_img, self.invader_shot]      # back_img correspond à l'image de fond
                    list_invaders = []          # liste qui va rassembler tous le aliens qui ne doivent pas pouvoir se tuer entre eux
                    for invader in invaders :    
                        inv = invader.invader_item
                        list_invaders.append (inv)
                    dont_want = dont_want + list_invaders   # liste qui rassemble tous les éléments que l'on ne veut pas supprimer quand les aliens tirent
                    if item not in dont_want :
                        if item == self.ship.player_item :
                            self.canevas.delete (self.invader_shot)
                            self.ship.add_score (-20)
                            self.ship.lost_life()
                            if self.ship.life == 0 :
                                self.suppr_figures (invaders)
                                messagebox.showinfo ("Perdu", "Vous n'avez plus de vies")
                                break
                        else :
                            self.canevas.delete (self.invader_shot)
                            self.canevas.delete (item)

        self.window.after (30, lambda : self.bullet_invaders (back_img, invaders))

    def suppr_figures (self, invaders) :
        for invader in invaders :
            self.canevas.delete (invader.invader_item)
        self.canevas.delete (self.ship.player_item)

class Missile_B :
    def __init__ (self, x, y, window, canevas, ship) :
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.speed_shot_b = 10
        self.boos_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'purple')

    def bullet_boss (self, back_img) :
        self.ship.add_score (150)