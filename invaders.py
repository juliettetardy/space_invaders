from PIL import Image, ImageTk
from missile import Missile_I
from random import randint
from tkinter import messagebox

class Invader :
    def __init__ (self, x, y, canevas, img_path) :
        self.canevas = canevas
        self.x = x
        self.y = y
        self.invader_pic = Image.open (img_path)
        self.invader_pic = self.invader_pic.resize ((100, 100))
        self.pic = ImageTk.PhotoImage (self.invader_pic)
        self.invader_item = self.canevas.create_image (self.x + 20, self.y + 20, image = self.pic)

    def get_position (self) :
        return self.canevas.coords (self.invader_item)

    def invaders_move (self, speed, moving_down) :
        if moving_down == 0 :
            self.canevas.move (self.invader_item, speed, 0)
        elif moving_down == 1 :
            self.canevas.move (self.invader_item, speed, 2)

class Invaders :
    def __init__ (self, window, canevas, ship, imgPath) :
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.imgPath = imgPath
        self.invaders = []
        self.speed = 4
 
    def add_invaders (self) :
        width_canvas = 1530
        height_aliens = 30
        for nmb_lines in range (1, 4) :
            if nmb_lines % 2 != 0 :
                # Coordonnées X,Y de chqaue alien :
                place_for5 = width_canvas / 5
                final_place_for5 = place_for5 - 20 - width_canvas / 10
                coord_for5 = [[final_place_for5, height_aliens], [final_place_for5 + place_for5, height_aliens], [final_place_for5 + 2 * place_for5, height_aliens], [final_place_for5 + 3 * place_for5, height_aliens], [final_place_for5 + 4 * place_for5, height_aliens]]
                i = 0
                while i < 5 :
                    x0, y0 = coord_for5 [i][0], coord_for5 [i][1]
                    invader = Invader (x0, y0, self.canevas, self.imgPath)
                    self.invaders.append (invader)
                    i += 1
            else : 
                # Coordonnées X,Y de chaque alien :
                place_for4 = width_canvas / 5
                final_place_for4 = place_for4 - 20 
                coord_for4 = [[final_place_for4, height_aliens], [final_place_for4 + place_for4, height_aliens], [final_place_for4 + 2 * place_for4, height_aliens], [final_place_for4 + 3 * place_for4, height_aliens]]
                i = 0
                while i < 4 :
                    x0, y0 = coord_for4 [i][0], coord_for4 [i][1]
                    invader = Invader (x0, y0, self.canevas, self.imgPath)
                    self.invaders.append (invader)
                    i += 1
            height_aliens += 80

    def move_invaders (self) :
        # permet d'inverser la vitesse de tous les aliens si celui le plus à droit ou le plus à gauche touche le bord du canva
        for invader in self.invaders :
            coord = invader.get_position()
            if len (coord) == 2 :
                if coord [0] + 20 >= 1530 or coord [0] - 20 <= 0 :
                    self.speed = - self.speed 
                    break

        # permet de faire descendre les aliens si ils tapents à gauche
        for invader in self.invaders :
            coord = invader.get_position()
            if len (coord) == 2 :
                if coord [0] - 40 <= 0 :
                    for invader in self.invaders :
                        invader.invaders_move (self.speed, 1)
                    break
                else :
                    invader.invaders_move (self.speed, 0)

        # permet de tuer le vaisseau/arrêter la partie si les aliens touchent le vaisseau ou le bas du canva
        for invader in self.invaders :
            coords = invader.get_position()
            if len (coords) == 2 :
                coord = [coords [0] - 20, coords [1] - 20] + coords
                contacts = self.canevas.find_overlapping (*coord)
                if coord [1] > 620 :
                    self.canevas.delete (invader.invader_item)
                    messagebox.showinfo ("Perdu", "Vous n'avez pas réussi à détruire tous les aliens")
                    self.ship.life = 0
                    self.canevas.delete (self.ship.player_item)
                    for invader in self.invaders :
                        self.canevas.delete (invader.invader_item)
                    break
                else : 
                    for item in contacts :
                        if item == self.ship.player_item :
                            self.canevas.delete (item)
                            self.canevas.delete (invader.invader_item)
                            self.ship.life = 0
                            messagebox.showinfo ("Perdu", "Vous avez été touché par un alien")
                            for invader in self.invaders :
                                self.canevas.delete (invader.invader_item)
                            break

        self.window.after(20, self.move_invaders)

    def shoot_ship (self, back_img) :
        for invader in self.invaders :
            can_move = randint(0, 250)
            if can_move == 250 :
                coord = invader.get_position()
                if len (coord) == 2 :
                    shot = Missile_I (coord[0] - 5, coord[1] + 40, self.window, self.canevas, self.ship)
                    shot.bullet_invaders (back_img, self.invaders)

        self.window.after (30, lambda : self.shoot_ship (back_img))
