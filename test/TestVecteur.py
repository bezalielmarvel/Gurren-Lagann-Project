from geometrie3D import Vecteur, Point
from math import *
v1=Vecteur(10,5,0)
v2=Vecteur(60,0,0)
a=Point(3,3,0)

print("{} * {} = {}".format(v1,v2,v1*v2))
print("{} + {} = {}".format(v1,v2,v1+v2))
print("{} - {} = {}".format(v1,v2,v1-v2))
print("{} ^ {} = {}".format(v1,v2,v1**v2))

print("\nConversions en point:")
print("1- {} + {} = {}".format(a, v1, a+v1))
print("2- type({}.toPoint()) = {}".format(v1, type(v1.toPoint()) ))

#rotation
n=3
teta=2*pi/n
angle=v1.getAngle2D()
print("\nv1 = {}".format(v1))
print("angle v1: {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))

print("{} rotation de {} radians/ {} degres de v1 = {}".format(n,teta, int(teta*360/(2*pi)), v1))

for i in range(0, n):
    v1.rotation2D(teta)
    print("\n|v1|= |{}| = {}".format(v1,v1.getNorme()))
    angle=v1.getAngle2D()
    print("angle de v1: {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))


