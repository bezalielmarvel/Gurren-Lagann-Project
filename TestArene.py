from geometrie3D.Arene import *
from geometrie3D.Polygone3D import *
from geometrie3D.Pave import *


#Creation d'une arene et ajout de n objets
a = Arene()
p = Pave(45,3,12)
poly = Polygone3D()
poly.sommets = [Point(14,15,14) , Point(5,99,120)]
a.add(poly)
a.add(p)
#a.sauvegarder("./geometrie3D/BanqueArenes/arene1.txt")
b = Arene()
#a.lecture_fichier("./geometrie3D/BanqueArenes/arene1.txt")
a.vueDessus(200,200)