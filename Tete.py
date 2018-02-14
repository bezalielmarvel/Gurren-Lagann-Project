from robotRep.Capteur import *
from robotRep.CapteurIR import *

class Tete : 
    def __init__( self , position , orientation ) :
        self.position = position
        self.orientation = orientation
        self.Capteurs = []

    def ajouterCapteur (self , capteur) :
        """cette méthode permet d'ajouter un capteur sur la tête, si elle n'a pas de capteur de même type 
        """
        if issubclass(type(Capteur) , capteur ) :
             #on doit vérifier si y'a pas un capteur de même type 
            for cap in self.Capteurs :
                if cap.type == capteur.type :
                    print("il y a deja un capteur de meme type sur cette tête!")
                    return
            self.Capteurs.append(capteur)

    def supprimerCapteur(self , typeCapteur) : 
        """on supprime un capteur on spécifiant son type 
        """
        for cap in self.Capteurs :
            if cap.type == typeCapteur :
                self.Capteurs.remove(cap)
                return