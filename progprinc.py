from game import Game
from tkinter import Tk, Canvas, NW

go = Game()
window = go.get_window()
canevas = go.get_canevas()

go.create_widgets (window)
go.create_figures (window, canevas)

window.mainloop()