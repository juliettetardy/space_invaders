from game import Game
from tkinter import Tk, Canvas, NW

go = Game()
window = go.get_window()
canevas = go.get_canevas()

img = go.get_background_img()
canevas.grid() 

go.create_widgets (window)
go.figure (window, canevas)

window.mainloop()