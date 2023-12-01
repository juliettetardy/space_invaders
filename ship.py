from PIL import Image, ImageTk

class Ship:

    def __init__(self, x, y, canevas, window, width, height, img_path): # Création du vaisseau et de sa position initiale
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        
        self.w = width/2
        self.h = height -70
        self.ship_pic = Image.open(img_path)
        self.ship_pic = self.ship_pic.resize((130,130))
        self.pic = ImageTk.PhotoImage(self.ship_pic)
        self.player_item = self.canevas.create_image(self.w, self.h, image = self.pic)

    def ship_move(self, delta):
        coord = self.canevas.coords(self.player_item)
        new_position = coord[0] + delta
        if 20 < new_position < 1495: 
            left = self.canevas.move(self.player_item, delta, 0) 
    


