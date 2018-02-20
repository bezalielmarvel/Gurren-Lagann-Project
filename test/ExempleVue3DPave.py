from affichage.troisD import *
from geometrie3D import *
from math import *

w=pyglet.window.Window(600,450)

# on cree le pave et on initialise sa position
p=Pave(50,50,0)
p.deplacer(Vecteur(100,100,0))

#creation de la vue
v=Vue3DPave(p)

#on tourne le pave, on met a jour la vue
p.tourner(pi/3)
v.update()

#si on redessine la fenetre, on redessine la vue du pave
@w.event
def on_draw():
    w.clear()
    v.draw()
    
    

pyglet.app.run()

