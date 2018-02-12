import sys
sys.path.append('..')

from geometrie3D import Arene
from geometrie3D import Objet3D
from geometrie3D import Polygone3D
from geometrie3D import trouverObjet3D
from geometrie3D.pointRep import Point




a=Arene()
o = Polygone3D()
v = Polygone3D()

#creation
o.addSommet(Point(0, 0, 0))
o.addSommet(Point(1, 0, 0))
o.addSommet(Point(0, 1, 0))
o.addSommet(Point(1, 1, 0))
#o.setCentre(Point(0, 0, 0))                 Il faut ajouter dans la classe polygone cette methode

#creation
v.addSommet(Point(2, 0, 0))
v.addSommet(Point(4, 0, 0))
v.addSommet(Point(0, 2, 0))
v.addSommet(Point(4, 4, 0))
#v.setCentre(Point(2,0,0))                 Meme commentaire qu'au dessus


a.add(o)
a.add(v)

listeResultat = trouverObjet3D(a, 3, 1, 0)

print(listeResultat)
