# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, Button


class Menu :
    def __init__(self,w,h):
    
        self.mainWindow = Tk()
        self.mainWindow.title('Tavern Invaders')
        self.mainWindow.geometry(f"{w}x{h}")
        self.Canvas = Canvas(self.mainWindow, width = 1280, height = 720, background = "#000144")

    
    def mainMenu(self): #Fenêtre du menu principal
        self.title = self.Canvas.create_text(640,360, fill = '#FF822C' ,text = 'Space Invaders' ,font = ("arial", 30))

        quit.pack(side = 'top' , padx = 0 , pady = 0)
        
        self.Canvas.pack(padx = 5,pady = 5)