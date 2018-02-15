from geometrie3D import Objet3D
from geometrie3D.pointRep import *
from geometrie3D.Polygone3D import *
from math import pi

class Pave(Polygone3D):
    """
    Classe definissant un pave dans un repere en 3D
    """
    def __init__(self, longueur, largeur, hauteur):
        """
        Constructeur ajoutant les 8 sommets autour du centre par defaut: (0,0,0)
        """
        Polygone3D.__init__(self)
        self.addSommet(Point(self.centre.x-longueur/2, self.centre.y-largeur/2, self.centre.z+hauteur/2))
        self.addSommet(Point(self.centre.x+longueur/2, self.centre.y-largeur/2, self.centre.z+hauteur/2))
        self.addSommet(Point(self.centre.x+longueur/2, self.centre.y+largeur/2, self.centre.z+hauteur/2))
        self.addSommet(Point(self.centre.x-longueur/2, self.centre.y+largeur/2, self.centre.z+hauteur/2))
        self.addSommet(Point(self.centre.x-longueur/2, self.centre.y-largeur/2, self.centre.z-hauteur/2))
        self.addSommet(Point(self.centre.x+longueur/2, self.centre.y-largeur/2, self.centre.z-hauteur/2))
        self.addSommet(Point(self.centre.x+longueur/2, self.centre.y+largeur/2, self.centre.z-hauteur/2))
        self.addSommet(Point(self.centre.x-longueur/2, self.centre.y+largeur/2, self.centre.z-hauteur/2))

    def tournerAutour(self, point, teta):
        """
        tourne le pave autour de point d'un angle teta
        """
        for i in range(0,len(self.sommets)):
            self.sommets[i].tournerAutour(point, teta)
    
        if point!=self.centre:
            self.centre.tournerAutour(point, teta)
    
    def tourner(self, teta):
        """
        tourne le pave autour du centre
        """
        self.tournerAutour(self.centre, teta)
