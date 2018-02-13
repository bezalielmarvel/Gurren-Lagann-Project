from geometrie3D import Arene

def trouverObjet3D(arene, x, y, z):
    """Cette fonctions permet de savoir si un pointRep de coordonnées x, y, z appartient a un objet 3D"""

    """On attribue aux differentes variables les valeurs du premier sommets"""
    listeObjet3D = arene.objets3D
    
    """La variable a permet d'acceder chaque objet dans liste d'objet 3D"""
    a = 0

    """La variable liste retour permet de retourner une liste contenant tout les objets dans lesquelles le point est present"""
    listeRetour = list()

    for i in listeObjet3D:
        listeSommets = listeObjet3D[a].sommets
        """On recupere tous les sommets de l'objet numero a """

        listeCoord = listeSommets[0]
        """On recupere toutes les coordoonnées du premier sommet"""

        min_x = listeCoord.x
        min_y = listeCoord.y
        min_z = listeCoord.z
        max_x = listeCoord.x
        max_y = listeCoord.y
        max_z = listeCoord.z

        for elt in listeSommets:
            listeCoord = elt
            """on recupere chaques coordonnées x, y, z de elt qui parcourt la liste de sommet"""

            if (listeCoord.x < min_x):
                min_x = listeCoord.x
            if (listeCoord.y < min_y):
                min_y = listeCoord.y
            if (listeCoord.z < min_z):
                min_z = listeCoord.z
            if (listeCoord.x > max_x):
                max_x = listeCoord.x
            if (listeCoord.y > max_y):
                max_y = listeCoord.y
            if (listeCoord.z > max_z):
                max_z = listeCoord.z

        if (((x >= min_x) and (x <= max_x)) and ((y >= min_y) and (y <= max_y)) and ((z >= min_z) and (z <= max_z))):
            print("Le pointRep de coordonnées {}, {}, {} appartient à un objet 3D ".format(x, y, z, ))
            listeRetour.append(i)
        else:
            print("Le pointRep de coordonnées {}, {}, {} n'appartient pas à un objet 3D ".format(x, y, z, ))
        a = a + 1

    return listeRetour
