from geometrie3D.Objet3D import *


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
        index = len(self.objets3D)-1

        while index >= 0:
            del self.objets3D[index]
            index -= 1



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

    def triObjets(self):
        def medHeight(obj):	
            zmax=0
            zmin=0
            for s in obj.sommets:
                if(s.z>zmax):
                    zmax=s.z
                if(s.z<zmin):
                    zmin=s.z
        return (float(zmin+zmax)/2.0)
#self.objets3D=sorted(self.objets3D,key=medHeight)
