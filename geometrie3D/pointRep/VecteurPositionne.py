from geometrie3D.pointRep import Point, Vecteur

class VecteurPositionne(Vecteur):
    """
    Vecteur avec une position dans l'espace
    """
    def __init__(self, vecteur, point):
        """
        vecteur: Vecteur representant la direction/norme du vecteur
        point: Point representant la position du vecteur
        """
        if issubclass(type(vecteur),Vecteur) and issubclass(type(point),Point):
            self.position=point
            self.vecteur=vecteur
    
    def collision2D(self, vecteurPos):
        """
        vecteurPos: VecteurPositionne
        
        renvoi True si les vecteurs se rencontrent dans le repere 2D
        """
        A=self.position
        B=self.position+self.vecteur
        M=vecteurPos.position
        N=vecteurPos.position+vecteurPos.vecteur
        if self.vecteur**vecteurPos.vecteur == Vecteur(0.0,0.0,0.0):
            if A != M and B != N:
                if (self.vecteur**(N-A).toVect())*(self.vecteur**(M-A).toVect())<=0:
                    if (vecteurPos.vecteur**(B-M).toVect())*(vecteurPos.vecteur**(A-M).toVect())<=0:
                        return True
        return False