from affichage.deuxD.interface.AppRobotAutonome import *
from robotRep.RobotAutonome import *
from affichage.deuxD.vue2DRep import *

r=RobotAutonome(Pave(50,50,0), Objet3D(), Objet3D(), Vecteur(0,-1,0))
r.stratDeplacement=DeplacementSimple(r)
r.deplacer(Vecteur(150,150,0))
a=Arene()
a.add(r)

app=AppRobotAutonome(r, Vue2DArene(a))
app.init() 

app.mainloop()

