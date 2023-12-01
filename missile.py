from ship import Ship

class Missile:

    def __init__(self, x, y, canevas):
        self.name = 'pewpew'
        if Missile.name == 'Player':
            self.direction = 1
        self.x = x
        self.y = y
        self.speed = 5
        self.canevas = canevas
        self.apparence = self.canevas.create_rectangle(self.x, self.y, self.x+5, self.y+10, width = 5, outline = 'black', fill = 'yellow')
    
    def missile(self, canevas, window):
        x1, y1, x2, y2 = canevas.coords(self.apparence)
        if y2 >= 495 or y1 <= 5:
            self.speed = - self.speed

        canevas.move(self.form, 0, self.speed)
        item_list = []
        item_list = canevas.find_all()
        for item in item_list:
            x1_item, y1_item, x2_item, y2_item = canevas.coords(item)
            if (x1 < x2_item and y1 < y2_item) and (x2 > x1_item and y2 < y1_item):
                canevas.delete(item)
                canevas.delete(self.apparence)
                return None
        window.after(60, lambda: self.missile(canevas, window))
        
        
         



        

        

    
   