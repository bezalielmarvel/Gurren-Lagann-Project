from .Objet3D import *
from .Pave import *
from .Polygone3D import *

class Arene(object):
    """
    Definit une structure de base pour une arene contenant des Objet3D
    """

    def __init__(self):
        """
        objets3D: [Objet3D]
        """
        self.objets3D = list()

    def add(self, objet3D):
        """
        Ajoute un objet3D a la liste si c'est une sous classe de Objet3D
        """
        if (issubclass(type(objet3D), Objet3D)):
            self.objets3D.append(objet3D)

    def vider(self):
        """
        Reinitialise la liste d'objets 3D
        """
        self.objets3D = list()


    def vueDessus(self, xmax, ymax):
        matrice2D = [[-1] * ymax for _ in range(xmax)]
        resolutionx = 0
        resolutiony = 0

        while(xmax/10):
            resolutionx += 1
        while(ymax/10):
            resolutiony += 1

        for a in self.objets3D:
            if isinstance(a, Polygone3D):
                listeSommets = a.sommets
                listeCoord = listeSommets[0]
                max_x = listeCoord.x
                max_y = listeCoord.y
                for elt in listeSommets:
                    """on recupere chaques coordonnées x, y, z de elt qui parcourt la liste de sommet"""
                    listeCoord = elt
                    if (listeCoord.x > max_x):
                        max_x = listeCoord.x
                    if (listeCoord.y > max_y):
                        max_y = listeCoord.y
            for i in range (listeCoord.x*(resolutionx*10), max_x * (resolutionx*10)):
                for j in range(listeCoord.y * (resolutiony*10), max_y * (resolutionx*10)):
                    matrice2D[i][j] = 1


    def sauvegarder(self , nomfichier):
        f = open(nomfichier , "w")
        f.write("1024 1024\n")
        for objet in self.objets3D :
            if issubclass(type(objet) , Pave) :
                f.write("PAVE {} {} {}".format(objet.longueur , objet.largeur,objet.hauteur))
            else :
                f.write("POLYGONE3D")
                for som in objet.sommets :
                    f.write(" ({},{},{})".format(som.x , som.y , som.z))
            f.write("\n")
        f.close()

    def lecture_fichier(self, fichier):
        """
        Cette cree une arene avec
        obstacles declaré dans un fichier txt.
        """

        mon_fichier = open(fichier, "r")
        for line in mon_fichier.read.splitlines()[1:]:
            words = line.split();
            if (words[0] == "POLYGONE3D"):
                polygone = Polygone3D()
                for sommet_str in words[2:]:
                    sommet_str = sommet.replace("(", "")
                    sommet_str = sommet.replace(")", "")
                    sommet_tab = sommet_str.split(",")
                    polygone.add(Point(sommet_tab[0], sommet_tab[1], sommet_tab[2]))
                self.add(polygone)
            elif (word[0] == "PAVE"):
                pave = Pave()
                for sommet in words[2:]:
                    sommet_str = sommet.replace("(", "")
                    sommet_str = sommet.replace(")", "")
                    sommet_tab = sommet_str.split(",")
                    pave.add(Point(sommet_tab[0], sommet_tab[1], sommet_tab[2]))
                self.add(pave)
        mon_fichier.close()

    def __repr__(self):
        """
        Quand on entre une arene dans l'interpreteur
        """
        return "Arene: objets3D({})".format(self.objets3D)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut

        si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans Arene !".format(nom))



