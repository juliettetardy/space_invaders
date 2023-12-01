"""drapeau = False"""

class Invaders :
    def __init__(self, window, canevas) :
        self.window = window
        self.canevas = canevas
        self.invaders = []
        self.speed = 5

    def add_invaders(self) :
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
                    invader = Invader(x0, y0, self.canevas)
                    self.invaders.append(invader)
                    i += 1
            else : 
                # Coordonnées X,Y de chaque alien :
                place_for4 = width_canvas/5
                final_place_for4 = place_for4 - 20 
                coord_for4 = [[final_place_for4, height_aliens], [final_place_for4 + place_for4, height_aliens], [final_place_for4 + 2*place_for4, height_aliens], [final_place_for4 + 3*place_for4, height_aliens]]
                i = 0
                while i < 4 :
                    x0, y0 = coord_for4[i][0], coord_for4[i][1]
                    invader = Invader(x0, y0, self.canevas)
                    self.invaders.append(invader)
                    i += 1
            height_aliens += 80

    def move_invaders(self) :
        for invader in self.invaders :
            if invader.get_position()[2] >= 1530 or invader.get_position()[0] <= 0 :
                self.speed = -self.speed
                break    
        for invader in self.invaders :
            invader.invaders_move(self.speed)
        self.window.after(20, self.move_invaders)

class Invader :
    def __init__(self, x, y, canevas) :
        self.canevas = canevas
        self.x = x
        self.y = y
        self.apparence = self.canevas.create_oval(self.x, self.y, self.x + 40, self.y + 40, width = 2, outline = 'black', fill = 'green') 

    def get_position(self) :
        return self.canevas.coords(self.apparence)

    def invaders_move(self, speed) :
        self.canevas.move(self.apparence, speed, 0)