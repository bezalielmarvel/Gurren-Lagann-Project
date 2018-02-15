from geometrie3D.pointRep import *

v=VecteurPositionne(Vecteur(10,0,0), Point(0,0,0))
v2=VecteurPositionne(Vecteur(0,-10,0), Point(5,5,0))

print("{} en collision avec {}: {}".format(v, v2, v.collision2D(v2)))