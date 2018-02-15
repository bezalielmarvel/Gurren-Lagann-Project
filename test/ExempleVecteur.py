from geometrie3D.pointRep import Vecteur, Point
from math import *

v1=Vecteur(10,20,0)
v3=v1.clone()
v2=(Point(-10,0,0)-Point(10,0,0)).toVect()
a=Point(2,6,8)

print("{} * {} = {}".format(v1,v2,v1*v2))
print("{} + {} = {}".format(v1,v2,v1+v2))
print("{} - {} = {}".format(v1,v2,v1-v2))
print("{} ^ {} = {}".format(v1,v2,v1**v2))
print("{} == {} = {}".format(v1,v2,v1==v2))
print("{} == {} = {}".format(v1,v3,v1==v3))

print("\nConversions en point:")
print("1- {} + {} = {}".format(a, v1, a+v1))
print("2- type({}.toPoint()) = {}".format(v1, type(v1.toPoint()) ))

#rotation
angle=v1.getAngle2D()
print("\nv1 = {}".format(v1))
print("angle v1: {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))

n=10
teta=2*pi/n
print("{} rotation de {} radians/ {} degres de v1 = {}".format(n,teta, int(teta*360/(2*pi)), v1))

for i in range(0, n):
    v1.rotation2D(teta)
    print("\n|v1|= |{}| = {}".format(v1,v1.getNorme()))
    angle=v1.getAngle2D()
    print("angle de v1: {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))

