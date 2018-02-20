import pyglet as pyg
from pyglet.gl import *
from geometrie3D import *

class Vue3DPave(object):
    """
    Permet de dessiner une repesentation 3D d'un pave en openGL
    """
    def __init__(self, pave, batch=None):
        """
        pave : Pave        
        sommets_data: Tuple
        self.index: [ int ]
        """
        self.pave=pave
        
        #definit les cotes avec kles indices des sommets: (0,1), (0,3) ...
        self.index=[0, 1, 0, 3, 0, 4, 1, 2, 1, 5, 2, 3, 2, 6, 3, 7, 4, 5, 4, 7, 5, 6, 6, 7]
        
        #concatenation des coordonnees des sommets
        self.sommets_data=()        
        for i in range(0, len(self.pave.sommets)):
            self.sommets_data+=self.pave.sommets[i].toTuple()
                       
    def draw(self):
        """
        dessine le pave dans la fenetre courante
        """
        pyglet.graphics.draw_indexed(8, pyglet.gl.GL_LINES, 
                                     self.index, ('v3f', self.sommets_data), ('c3B', (255,255,255)*8) ) # les lignes sont blanches
    def update(self):
        """
        met a jour les coordonnees du pave
        """
        self.sommets_data=()
        for i in range(0, len(self.pave.sommets)):
            self.sommets_data+=self.pave.sommets[i].toTuple()
