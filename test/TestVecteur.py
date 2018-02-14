from geometrie3D import Vecteur, Point
import unittest
from math import *

class TestVecteur(unittest.TestCase):

    def setUp(self):
        self.v1 = Vecteur(10, 5, 0)
        self.v2 = Vecteur(60, 0, 0)
        self.a = Point(3, 3, 0)
        self.n = 3
        self.teta = 2 * pi / self.n

    def test_initialisation(self):
        self.assertIsInstance(self.v1, Vecteur, msg=None)
        self.assertEqual(self.v1.x, 10)
        self.assertEqual(self.v1.y, 5)
        self.assertEqual(self.v1.z, 0)

    def test_getNorme(self):
        v = self.v1.getNorme()
        self.assertEqual(v, sqrt(pow(self.v1.x, 2) + pow(self.v1.y, 2) + pow(self.v1.z, 2)))

    def test_toPoint(self):
        v = self.v1.toPoint()
        self.assertIsInstance(v, Point, msg=None)

    def test_rotation2D(self):
        x = self.v1.x
        self.v1.rotation2D(self.teta)
        self.assertEqual(self.v1.x, x*cos(self.teta)-self.v1.y*sin(self.teta))




"""print("{} * {} = {}".format(v1,v2,v1*v2))
print("{} + {} = {}".format(v1,v2,v1+v2))
print("{} - {} = {}".format(v1,v2,v1-v2))
print("{} ^ {} = {}".format(v1,v2,v1**v2))

print("\nConversions en point:")
print("1- {} + {} = {}".format(a, v1, a+v1))
print("2- type({}.toPoint()) = {}".format(v1, type(v1.toPoint()) ))

#rotation
angle=v1.getAngle2D()
print("\nv1 = {}".format(v1))
print("angle v1: {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))

print("{} rotation de {} radians/ {} degres de v1 = {}".format(n,teta, int(teta*360/(2*pi)), v1))

for i in range(0, n):
    v1.rotation2D(teta)
    print("\n|v1|= |{}| = {}".format(v1,v1.getNorme()))
    angle=v1.getAngle2D()
    print("angle de v1: {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))"""


