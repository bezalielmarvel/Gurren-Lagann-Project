from geometrie3D.pointRep import *
""" 
p, p2 : Point
v, v2 : Vecteur
vp, vp2: VecteurPositionne
"""

p=Point(0,0,0)
v=Vecteur(10,0,0)
p2=Point(5,5,0)
v2=Vecteur(0,-10,0)

vp=VecteurPositionne(v, p)
vp2=VecteurPositionne(v2, p2)

print("{} en collision avec {}: {}\n".format(vp, vp2, vp.collision2D(vp2)))

print("Variante avec des points:")
print("collision( {}, {}, {}, {} ) = {} ".format(p, p+v, p2, p2+v2, collision(p, p+v, p2, p2+v2)))