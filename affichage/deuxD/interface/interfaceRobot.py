from tkinter import *
from geometrie3D import Arene, Pave, Objet3D
from affichage.deuxD.vue2DRep.Vue2D import *
from geometrie3D.pointRep import Vecteur
from robotRep import Robot
from math import *

"""
lance une simulation representant un robot de base
"""
arene=Arene()
robot=Robot(Pave(50, 50, 0), Objet3D(), Objet3D(), Vecteur(0,-1,0))
robot.deplacer(Vecteur(100,100,0)) #Le robot doit avoir une position nulle au depart pour etre a (50,50)
arene.add(robot)
vueArene=Vue2DArene(arene)

fenetre=Tk()
Canevas = Canvas(fenetre, width = 480, height = 320, bg ='white')

#Variables gerant le parametrage par l'utilisateur
Vitesse = StringVar()
Vitesse.set(2.0)
VitesseRot = StringVar()
VitesseRot.set(pi/50.0)
VMAX_ROT = StringVar()
VMAX_ROT.set(pi/10.0)
VMAX = StringVar()
VMAX.set(10.0)


def lancerSimulation():
    """
    Initialise les elements necessaires au lancement et appelle les fonctions de la simulation
    """

    #creaction fenetre
    fenetre.title("Interface d'affichage d'un prototype de robot")

    #creaction des boutons
    Button(fenetre, text ='Quitter', command = fenetre.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(fenetre, text ='Effacer', command = effacer).pack(side=LEFT,padx = 5,pady = 5)

    #attribution touches
    Canevas.bind('<q>', virageGauche)
    Canevas.bind('<d>', virageDroite)
    Canevas.bind('<z>', marcheAvant)
    Canevas.bind('<s>', marcheArriere)
    Canevas.focus_set()
    #preparation de la modulation de la vitesse
    modulVitesses()
    
    Canevas.pack(padx=10,pady=10)
    fenetre.mainloop()
    

def modulVitesses():
    """
    Cree les modulateurs de vitesse et de vitesse de rotation
    """
    # Creation d'un widget Spinbox
    boiteV1 = Spinbox(fenetre,from_=0,to=float(VMAX.get()),increment=0.5,textvariable=Vitesse,width=5,command=update)
    boiteV1.pack(padx=10,pady=10)
    Label(fenetre,text="Vitesse").pack(padx=10,pady=10)
    
    # Creation d'un widget Spinbox
    boiteV2 = Spinbox(fenetre,from_=0,to=float(VMAX_ROT.get()),increment=0.01,textvariable=VitesseRot,width=5,command=update)
    boiteV2.pack(padx=10,pady=10)
    Label(fenetre,text="Vitesse rotation").pack(padx=10,pady=10)

def update():
    """
    Met a jour les vitesses
    """
    robot.vitesse=float(Vitesse.get())
    robot.vitesseRot=float(VitesseRot.get())
    vueArene.afficher(Canevas)
    
def marcheAvant(event):
    update()
    effacer()
    robot.avancer()
    vueArene.afficher(Canevas)
def marcheArriere(event):
    update()
    effacer()
    if robot.vitesse>0:
        robot.vitesse=-robot.vitesse
    robot.avancer()
    vueArene.afficher(Canevas)
def virageGauche(event):
    update()
    effacer()
    if robot.vitesseRot>0:
        robot.vitesseRot=-robot.vitesseRot
    robot.tourner()
    vueArene.afficher(Canevas)
def virageDroite(event):
    update()
    effacer()
    robot.tourner()
    vueArene.afficher(Canevas)
    
def effacer():
    """
    Efface la zone graphique
    """
    Canevas.delete(ALL)

lancerSimulation()

