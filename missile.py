# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import messagebox

class Missile_S :
    """
    Une classe qui permet au joueur de tirer des missiles.
    Cette classe s'occupe de tous les éléments graphiques vis à vis des missiles et la gestion des colisions.

    Fonctions 
    ---------
        bullet_ship : 
            Permet au vaisseau d'envoyer un missile.

    """

    def __init__ (self, x, y, window, canevas, ship) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): 
            x : 
                coordonées en abscisse d'un missile
                type = int
            y : 
                coordonées en ordonnée d'un missile
                type = int
            window : 
                fenêtre contenant le jeu
                type = Tk
            canevas : 
                canevas du jeu sur lequel le missile va se déplacer
                type = Canvas
            ship : 
                Joueur/ vaisseau
                type = str

        Sortie(s): None

        """
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.speed_shot_s = - 15
        self.ship_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'brown')
        
    def bullet_ship (self, back_img, invaders) :
        """ 
        Fonction qui permet au vaisseau de tirer un missile
        Entrée(s): 
            back_img :
                Image de fond du jeu 
                type = PhotoImage
        Sortie(s): 
            self.canevas.coords : 
                Coordonnées sur le canva de l'alien
                type = list

        """
        self.canevas.move (self.ship_shot, 0, self.speed_shot_s)

        # Récupération des coordonées 
        coord = self.canevas.coords (self.ship_shot)
        if len (coord) == 4 :

            # On regarde si les coordonées sont similaires / si il y a contact
            contacts = self.canevas.find_overlapping (*coord)
            if coord [3] < 0 :

                # Si contact, on supprime 
                self.canevas.delete (self.ship_shot)

            for item in contacts :

                # On ne supprime pas le fond
                if item not in [back_img, self.ship_shot] : 
                    self.canevas.delete (self.ship_shot)
                    self.canevas.delete (item)
                    if item in invaders :
                        invaders.remove (item)

                    # Ajout du score car contact 
                    self.ship.add_score (10)  

        # La fonction attend un délai et ne s'exécute pas tout de suite
        self.window.after (30, lambda : self.bullet_ship (back_img, invaders))

class Missile_I :
    """
    Une classe qui permet aux aliens de tirer des missiles.
    Cette classe s'occupe de tous les éléments graphiques vis à vis des missiles et la gestion des colisions.

    Fonctions 
    ---------
        bullet_invaders : 
            Fonction qui permet aux aliens de tirer des missiles
    
        suppr_figures :
             Fonction qui permet de supprimer les aliens et le vaisseau

    """
    def __init__ (self, x, y, window, canevas, ship) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): 
            x : 
                coordonées en abscisse d'un missile
                type = int
            y : 
                coordonées en ordonnée d'un missile
                type = int
            window : 
                fenêtre contenant le jeu
                type = Tk
            canevas : 
                canevas du jeu sur lequel le missile va se déplacer
                type = Canvas
            ship : 
                Joueur/ vaisseau
                type = str

        Sortie(s): None

        """
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.speed_shot_i = 10
        self.invader_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'green')
    
    def bullet_invaders (self, back_img, invaders) :
        """ 
        Fonction qui permet aux aliens de tirer des missiles 
        Entrée(s): 
            back_img :
                Correspond à l'image de fond du canevas
                type = PhotoImage
            invaders : 
                Les invaders représentent les aliens sur le canevas
                
        Sortie(s): None

        """

        self.canevas.move (self.invader_shot, 0, self.speed_shot_i)

        # Récupération des coordonnées des aliens (missiles)
        coord = self.canevas.coords (self.invader_shot)

        if len (coord) == 4 :
            contacts = self.canevas.find_overlapping (*coord)

            # Cas où il y a contact
            if coord [3] < 0 :
                # Supression du canevas
                self.canevas.delete (self.invader_shot)
            else :
                for item in contacts :
                    dont_want = [back_img, self.invader_shot] 

                    # Liste qui va rassembler tous le aliens qui ne doivent pas pouvoir se tuer entre eux
                    list_invaders = []          
                    for invader in invaders :    
                        inv = invader.invader_item
                        list_invaders.append (inv)

                    # liste qui rassemble tous les éléments que l'on ne veut pas supprimer
                    dont_want = dont_want + list_invaders 

                    # Si pas dans la liste, on peut le supprimer, modifier le score et les vies
                    if item not in dont_want :

                        if item == self.ship.player_item :
                            self.canevas.delete (self.invader_shot)
                            self.ship.add_score (-20)
                            self.ship.lost_life()
                            if self.ship.life == 0 :
                                self.suppr_figures (invaders)
                                messagebox.showinfo ("Perdu", "Vous n'avez plus de vies")
                                break
                        else :
                            self.canevas.delete (self.invader_shot)
                            self.canevas.delete (item)

        # délai avant de réaliser la fonction pour qu'elle ne s'exécute pas tout de suite
        self.window.after (30, lambda : self.bullet_invaders (back_img, invaders))

    def suppr_figures (self, invaders) :
        """ 
        Fonction qui permet de supprimer les aliens et le vaisseau
        Entrée(s): 
            invaders : 
                Les invaders représentent les aliens sur le canevas

        Sortie(s): None

        """
        # Suppression de chaque aliens
        for invader in invaders :
            self.canevas.delete (invader.invader_item)

        # Suppression du vaisseau
        self.canevas.delete (self.ship.player_item)

class Missile_B :
    def __init__ (self, x, y, window, canevas, ship) :
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.speed_shot_b = 10
        self.boos_shot = self.canevas.create_rectangle (self.x, self.y, self.x + 5, self.y + 10, width = 5, outline = 'purple')

    def bullet_boss (self, back_img) :
        self.ship.add_score (150)