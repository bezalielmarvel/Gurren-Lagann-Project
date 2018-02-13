from robotRep.strategie.deplacement import StrategieDeplacement
from robotRep import *

class DeplacementSimple(StrategieDeplacement):
    def __init__(self, robot):
        """
        initialisation avec la classe mere
        """
        StrategieDeplacement.__init__(self, robot)
        
    def deplacementVers(self, destination):
        """
        le robot excute un mouvement de rotation, puis avance vers la destination
        """
        v=(destination-self.robot.centre).toVect()
        distance=v.getNorme()
        diffAngle=self.robot.direction.diffAngle2D(v)
        if distance>10:
            if abs(diffAngle)>self.robot.vitesseRot:
                self.robot.tourner(diffAngle)
            else :
                self.robot.avancer(1)  
        else:
            self.robot.destination=None
            

    def deplacementRel(self, vecteur):
        """
        le robot excute un mouvement direct vers la destination indiquee par vecteur
        """
        self.deplacementVers(self.robot.centre+vecteur)