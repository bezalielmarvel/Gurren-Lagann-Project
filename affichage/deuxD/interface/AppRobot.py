from tkinter import *
from robotRep import *
from geometrie3D import *
from affichage.deuxD.vue2DRep import *

class AppRobot(Tk):
    """
    Definit une structure d'affichage d'un robot dans une arene vide
    """
    def __init__(self, robot, arene):
        """
        Constructeur de l'application
        
        robot: Robot
        arene: vue de l'arene (avec methode afficher())
        """
        Tk.__init__(self)
        self.robot=robot    
        self.arene=arene
        self.canvas=Canvas(self, width = 480, height = 320, bg ='white')    
        
        #Variables gerant le parametrage par l'utilisateur
        #vitesses du robot suit ses valeurs
        self.vitesse = StringVar()
        self.vitesse.set(2.0)
        self.vitesseRot = StringVar()
        self.vitesseRot.set(pi/50.0)
        VMAX_ROT = StringVar()
        VMAX_ROT.set(pi/10.0)
        VMAX = StringVar()
        VMAX.set(10.0)        
        
        # Creation widgets Spinbox
        boiteV1 = Spinbox(self,from_=0,to=float(VMAX.get()),increment=0.5,textvariable=self.vitesse,width=5,command=self.update)
        boiteV1.pack(side="left",padx=10,pady=10)
        Label(self,text="Vitesse").pack(side="left",padx=10,pady=10)
        boiteV2 = Spinbox(self,from_=0,to=float(VMAX_ROT.get()),increment=0.01,textvariable=self.vitesseRot,width=5,command=self.update)
        boiteV2.pack(side="left",padx=10,pady=10)
        Label(self,text="Vitesse rotation").pack(side="left",padx=10,pady=10)

        #gestion des eventements pour commander le robot
        self.canvas.bind('<Key>', self.keyCommand)
        self.canvas.focus_set()
        
        self.canvas.pack()
        
    def keyCommand(self, event):
        """
        dirige le robot selon la touche tapee
        """
        self.update()
        self.canvas.delete(ALL)
        touche=event.keysym
        if touche=='z':
            self.robot.avancer(1)
        elif touche=='s':
            self.robot.avancer(-1)
        elif touche=='q':
            self.robot.tourner(1)
        elif touche=='d':
            self.robot.tourner(-1)
        self.arene.afficher(self.canvas)
            
    def update(self):
        """
        Met a jour les vitesses
        """
        self.robot.vitesse=float(self.vitesse.get())
        self.robot.vitesseRot=float(self.vitesseRot.get())
        self.arene.afficher(self.canvas)
        