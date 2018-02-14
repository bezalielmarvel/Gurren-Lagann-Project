from robotRep.Robot import *
from robotRep.Tete import *

class RobotPhysique (Robot):
    def __init__(self , pave , rg ,rd , direction ):
        Robot.__init__(pave , rg , rd , direction)
        self.tete = Tete(pave.centre , direction) # la tete est exactement au centre du robot, elle est orienté comme le vecteur direction 

    
