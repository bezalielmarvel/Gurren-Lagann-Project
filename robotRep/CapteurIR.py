from robotRep.Capteur import *
from math import *
from geometrie3D.pointRep import Vecteur
from geometrie3D.pointRep import Point

class CapteurIR (Capteur) :
    """un capteur de distance, calcule la distance entre le point position et un Polygone,
        les émissions IR se font sur un axe donné par un vecteur orientation,
        si le signal envoyé par le capteur celon ce vecteur croise un polygone dans l'arene, une exxeption sera lancée
    """
    def __init__(self , position, portee , orientation):
        Capteur.__int__(position , orientation)
        self.type = "IR"
        self.portee = portee
        self.pointMax = Point(cos(orientation.getAngle2D()) * self.portee + 
            position.x , sin ( orientation.getAngle2D()) * self.portee + position.y , 0) 

    def coolision(self , arene ):
        """ cette methode retournera True si ya une coolision probable entre un objet3D dans l'arene et le robot
            si cet objet est à porté du capteur, il sera detecté.
            le principe consiste a faire une projection des objet qui sont devant le capteur sur le plan
            OXY, et voir si ya des coolisions etre un vecteur orientation, et le veceurs des sommets de l'objet pris deux
            à deux """
        for objet3D in arene.objets3D :
            if devant(objet.centre) :
                if mesure(self.orientation , objet3D) > 0 :
                    return True 
        return False

    def devant( self , point) :
        """cette méthode retroune True si la projection sur OXY d'un point est devant le capteur
        retroune False sinon
        """
        vecttemp = Vecteur(point.x - self.position.x , point.y - self.position.y , 0)
        return orientation.mul(vecttemp) > 0 

    def collisionVecteur(pointA ,pointB , pointC , pointD) : #coolision entre les vecteurs AB et CD
       """cette méthode permet de dire si deux segment AB et CD sont en collisions, 
       dans ce cas elle doit retourner True
       sinon elle retournera Faux
       """
       E=Vecteur(pointB.x-pointA.x,pointB.y-pointA.y,0)	
       F=Vecteur(pointD.x-pointC.x,pointD.y-pointC.y,0)
       #z=0 car on travail en 2D
       denom=E.x*F.y-E.y*F.x
       if(denom==0):
           return False
       t=-(float)(pointA.x*F.y-pointC.x*F.y-F.x*pointA.y+F.x*pointC.y)/denom
       u=-(float)(-E.x*pointA.y+E.x*pointC.y+E.y*pointA.x-E.y*pointC.x)/denom
       if(u<0 or u>1)or(t<0 or t>1):
           return False
       else:
           return True     

    def mesure(vecteur, objet3D) :
        """ cette méthode retournera la distance si ya une colision entre le vecteur et l'objet3D
            sinon elle retournera -1 
            notre objet3D doit etre un polygone avec plusieurs sommets
        """
        sommetsProbables = []  #liste des sommets qui sont devant le centre de l'objet3D
        listeSegments = []  #liste des segments, un segment est un couple de point
        if issubclass(type(objet3D) , Polygone) :
            vectObjet = Vecteur (-vecteur.x , -vecteur.y , 0)
            if len(objet3D.sommets) > 0 :
                for sommet in objet3D.sommets :
                    if vectObjet.mul(Vecteur(sommet.x - objet3D.centre.x , sommet.y , objet3D.centre.y , 0)) > 0 :
                        #dans un premier temps, on garde uniquement les sommets devant le centre de l'objet3D    
                        sommetsProbables += sommet
                if len(sommetsProbables) < 2 :
                    #on test tout les sommets 
                    sommetsProbables = objet3D.sommets
                if len(sommetsProbables) > 1 :
                    # notre objet n'est pas formé uniquement d'un point
                    #on essaye de trier notre liste de sommets celon y, pour pouvoir tester segment par segment
                    sommetsProbables.sort(Point.y)
                    j = 0
                    for i in range(1 , len(sommetsProbables)):
                        if coolisionVecteur(self.position , self.pointMax , sommetsProbables[i] , sommetsProbables[j]) :
                            listeSegments += (sommetsProbables[i] , sommetsProbables[j])
                    if len(listeSegments) > 0 :
                        #on calcule la distance entre chaque point de coolision et la position du capteur
                        alpha  = vecteur.y / vecteur.x 
                        beta = position.y - alpha * position.x
                        for segment in listeSegments :
                            ceof = (segment[1].y - segment[0].y) / (segment[1].x - segment[0].x)
                            cordX = (segment[1].y - beta - ceof)/ (alpha - ceof)
                            pointCol = Point(cordX , alpha * cordX + beta , 0)
                            listeDistances += sqrt(pow(pointCol.x - position.x, 2) + pow(pointCol.y - position.y, 2))
                        return min(listeDistances) 
                    else :
                        return -1
            else :
                return -1


        
        
