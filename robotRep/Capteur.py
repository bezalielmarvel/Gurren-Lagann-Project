
class Capteur :
    """classe abstraites contient une méthode de mesure a redifinire celon le type du capteur
        et un atribut type pour savoir quel type de capteur il s'agit
        position qui est un point
    """
    def __int__(self , position, orientation):
        self.type = "capteur"
        self.position = position
	    self.orientation = orientation

    def __repr__(self):
        print(" capteur de type : {} , position : {} ".format(self.type , self.position))

