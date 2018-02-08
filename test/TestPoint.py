from geometrie3D.pointRep import *


A=Point(0,0,0)
B=Point(1,2,3)
C=Vecteur(1,2,3)

A.setPosition(Point(0,0,1))
A.deplacer(Point(0,1,0))
print("deplacement de {}".format(A))
print("coordonnee y: {}\n".format(A.y))

print("{} + {} = {}".format(A,B,A+B))
print("{} - {} = {}".format(A,B,A-B))
print("{} / 2 = {}\n".format(A,A/2))
print("conversions en vecteur:")
print("{} + {} = {}".format(C,A,C+A))
print("type({}.toVect()) = {}".format(A, type(A.toVect()) ))
