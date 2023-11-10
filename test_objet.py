from tkinter import Tk, Canvas ,Button ,Label

class Mywindow():

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Space Invaders Ju2 version')
        self.Canevas = Canvas(self.main_window, width = 1280, height = 720, background = 'white')

    def menu(self): 
        new_game = Button(self.main_window ,text = "New game")
        quit = Button(self.main_window ,text = "Quit" ,command = self.main_window.destroy)
        lives = Label(self.main_window ,text = "lives : ")     
        self.title = self.Canevas.create_text(640,360 ,text = 'Space Invaders Ju2 version')

        quit.pack()
        new_game.pack()
        lives.pack()
        self.Canevas.pack(padx = 5,pady = 5)

class Ship:
    def __init__(self):
        self.x = PosX
        self.y = PosY
        self.apparence = canevas.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, width = 5, outline = 'black', fill = 'red')
    
    

main_window.mainloop()