import unittest

from geometrie3D import trouverObjet3D
from geometrie3D import Arene
from geometrie3D import Polygone3D
from geometrie3D.pointRep import Point


class testTrouverObjet(unittest.TestCase):
    """On initialise les propriétés de la classe"""

    a = Arene()
    o = Polygone3D()
    v = Polygone3D()

    o.addSommet(Point(0, 0, 0))
    o.addSommet(Point(1, 0, 0))
    o.addSommet(Point(0, 1, 0))
    o.addSommet(Point(1, 1, 0))

    v.addSommet(Point(2, 0, 0))
    v.addSommet(Point(4, 0, 0))
    v.addSommet(Point(0, 2, 0))
    v.addSommet(Point(4, 4, 0))

    a.add(o)
    a.add(v)



    def test_Instance(self):
        """On verifie si l'instance retourné est bien un polygone"""
        element = trouverObjet3D(self.a, 3, 1, 0)
        self.assertIsInstance(element[0], Polygone3D, msg=None)

    def test_Retour(self):
        element = trouverObjet3D(self.a, 3, 1, 0)
        self.assertEqual(element[0].x, 2)


if __name__ ==  '__main__ ' :
    unittest.main()

