from geometrie3D import Objet3D
from geometrie3D import Polygone3D
from geometrie3D.Arene import *
from geometrie3D.pointRep import *

o1=Polygone3D()
o2=Polygone3D()
o3=Polygone3D()

a=Point(0,0,0)
b=Point(25,25,25)
c=Point(50,50,50)
d=Point(75,75,75)

o1.addSommet(a)
o1.addSommet(b)
o1.addSommet(c)
o1.addSommet(d)

a=Point(100,100,100)
b=Point(125,125,125)
c=Point(150,150,150)
d=Point(175,175,175)

o2.addSommet(a)
o2.addSommet(b)
o2.addSommet(c)
o2.addSommet(d)

a=Point(200,200,200)
b=Point(225,225,225)
c=Point(250,250,250)
d=Point(275,275,275)

o3.addSommet(a)
o3.addSommet(b)
o3.addSommet(c)
o3.addSommet(d)

a1=Arene()
a2=Arene()
a3=Arene()

a1.add(o1)
a1.add(o2)
a1.add(o3)

a2.add(o3)
a2.add(o2)
a2.add(o1)

a3.add(o3)
a3.add(o1)
a3.add(o2)

print("\nAvant le tri:\n")
print(a1,"\n")
a1.triObjets()
print("Aprés le tri:\n")
print(a1,"\n")
print("Avant le tri:\n")
print(a2,"\n")
a2.triObjets()
print("")
print("Aprés le tri:\n")
print(a2,"\n")
print("Avant le tri:\n")
print(a3,"\n")
a3.triObjets()
print("Aprés le tri:\n")
print(a3)

