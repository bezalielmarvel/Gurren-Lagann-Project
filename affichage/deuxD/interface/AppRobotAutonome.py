from affichage.deuxD.interface import AppRobot
from geometrie3D import *
from robotRep import *
from time import sleep
from tkinter import *

class AppRobotAutonome(AppRobot):
    def __init__(self, robot, arene):
        AppRobot.__init__(self, robot, arene)
        self.canvas.bind('<Button-1>', self.setDestRobot)
        self.canvas.bind('<Button-2>', self.stopRobot)
        self._thread=None
        self._commandesClavier=False

    def keyCommand(self, event):
        """
        dirige le robot selon la touche tapee, et lui donne une destination avec la sourie
        """
        self.robot.destination=None
        self._commandesClavier=True
        
        self.update()

        touche=event.keysym
        if touche=='z':
            self.robot.avancer(1)
        elif touche=='s':
            self.robot.avancer(-1)
        elif touche=='q':
            self.robot.tourner(1)
        elif touche=='d':
            self.robot.tourner(-1)

        self.update()
        
        
    def setDestRobot(self, event):
        """
        donne une destination au robot, et lui fait executer la trajectoire
        """
        self._commandesClavier=False
        x=event.x
        y=event.y
        self.robot.destination=Point(x, y, 0)
        self.actionRobot()
        
        
    def actionRobot(self):
        self.update()
        sleep(0.1)
        if not self.robot.destination is None:
            self.actionRobot()
        
    def stopRobot(self):
        self.robot.destination=None
        self._commandesClavier=True
        
        
    def updateValues(self):
        """
        Met a jour les vitesses, et la position du robot
        """
        self.robot.vitesse=float(self.vitesse.get())
        self.robot.vitesseRot=float(self.vitesseRot.get())
    
    def updateCanvas(self):
        """
        Met a jour le canvas
        """
        self.canvas.delete(ALL)
        self.arene.afficher(self.canvas)
        self.canvas.update()

    def update(self):
        self.updateValues()
        self.updateCanvas()
        self.robot.update()