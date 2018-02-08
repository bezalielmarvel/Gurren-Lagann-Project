from geometrie3D import Arene, Objet3D



a=Arene()
n=3
b=Objet3D()

for i in range(0,n):
    a.add(Objet3D())
print(a)

#on vide l'arene 
a.vider()
print(a)

a.add(b)
print(a)
