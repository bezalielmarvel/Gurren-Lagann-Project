from geometrie3D.Objet3D import *
from geometrie3D import Polygone3D
from geometrie3D import pointDansPolygone

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





    def vueDessus(self, xmax, ymax):
        matrice2D = [[-1] * ymax for _ in range(xmax)]
        resolutionx = 0
        resolutiony = 0
        boolean = False

        """On regarde combien de chiffres possede xmax et ymax pour determiner la resolution de la matrice"""
        while(xmax/10):
            resolutionx += 1
        while(ymax/10):
            resolutiony += 1

        for a in self.objets3D:
            if isinstance(a, Polygone3D):
                listeSommets = a.sommets
            for i in range(0, xmax * (resolutionx*10)):
                for j in range(0, ymax * (resolutionx*10)):
                    boolean = pointDansPolygone(i, j, listeSommets)
                    if(boolean):
                        matrice2D[i][j] = 1
