import tkinter as tk
from PIL import Image, ImageTk

class MovingElement(tk.Canvas):
    def __init__(self, master, image_path, x, y, speed):
        super().__init__(master, width=50, height=50)  # Définir la taille du canvas
        self.master = master
        self.x = x
        self.y = y
        self.speed = speed

        # Charger l'image à partir d'un fichier .png
        self.image = Image.open(image_path)
        self.image = self.image.resize((50, 50), Image.ANTIALIAS)  # Redimensionner l'image si nécessaire
        self.photo = ImageTk.PhotoImage(self.image)

        # Créer un élément image à partir de l'image chargée
        self.element = self.create_image(self.x, self.y, anchor=tk.NW, image=self.photo)

        # Planifier l'appel de la méthode de déplacement
        self.after(20, self.move_element)

    def move_element(self):
        # Déplacer l'élément
        self.x += self.speed
        self.coords(self.element, self.x, self.y)

        # Inverser la direction si l'élément atteint les bords du canvas
        if self.x <= 0 or self.x >= self.master.winfo_width():
            self.speed = -self.speed

        # Planifier le prochain appel de move_element
        self.after(20, self.move_element)

# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Moving Element Example")

# Créer une instance de la classe MovingElement avec une image .png
element = MovingElement(fenetre, "chemin/vers/votre/image.png", x=50, y=50, speed=3)
element.pack()

# Lancer la boucle principale Tkinter
fenetre.mainloop()