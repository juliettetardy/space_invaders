from PIL import Image, ImageTk

drapeau = False
class Invaders :
    def __init__ (self, window, canevas, imgPath) :
        self.window = window
        self.canevas = canevas
        self.imgPath = imgPath
        self.invaders = []
        self.speed = 5
 
    def add_invaders (self) :
        width_canvas = 1530
        height_aliens = 30
        for nmb_lines in range(1,4) :
            if nmb_lines%2 != 0 :
                # Coordonnées X,Y de chqaue alien :
                place_for5 = width_canvas/5
                final_place_for5 = place_for5 - 20 - width_canvas/10
                coord_for5 = [[final_place_for5, height_aliens], [final_place_for5 + place_for5, height_aliens], [final_place_for5 + 2*place_for5, height_aliens], [final_place_for5 + 3*place_for5, height_aliens], [final_place_for5 + 4*place_for5, height_aliens]]
                i = 0
                while i < 5 :
                    x0, y0 = coord_for5[i][0], coord_for5[i][1]
                    invader = Invader (x0, y0, self.canevas, self.imgPath)
                    self.invaders.append (invader)
                    i += 1
            else : 
                # Coordonnées X,Y de chaque alien :
                place_for4 = width_canvas/5
                final_place_for4 = place_for4 - 20 
                coord_for4 = [[final_place_for4, height_aliens], [final_place_for4 + place_for4, height_aliens], [final_place_for4 + 2*place_for4, height_aliens], [final_place_for4 + 3*place_for4, height_aliens]]
                i = 0
                while i < 4 :
                    x0, y0 = coord_for4[i][0], coord_for4[i][1]
                    invader = Invader (x0, y0, self.canevas, self.imgPath)
                    self.invaders.append (invader)
                    i += 1
            height_aliens += 80

    def move_invaders (self) :
        for invader in self.invaders :
            if invader.get_position()[0] + 20 >= 1530 or invader.get_position()[0] - 20 <= 0 :
                self.speed = -self.speed
                break    
        for invader in self.invaders :
            invader.invaders_move (self.speed)
        self.window.after (20, self.move_invaders)

class Invader :
    def __init__ (self, x, y, canevas, img_path) :
        self.canevas = canevas
        self.x = x
        self.y = y
        self.invader_pic = Image.open (img_path)
        self.invader_pic = self.invader_pic.resize ((70, 70))
        self.pic = ImageTk.PhotoImage (self.invader_pic)
        self.invader_item = self.canevas.create_image (self.x + 20, self.y + 20, image = self.pic)

    def get_position (self) :
        return self.canevas.coords (self.invader_item)

    def invaders_move (self, speed) :
        self.canevas.move (self.invader_item, speed, 0)