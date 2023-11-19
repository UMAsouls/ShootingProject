import pygame
from pygame.locals import *
import os

#pythonでは実行ディレクトリがroot
#src内のものをimportするためカレントディレクトリ移動
os.chdir("../..")

from IKey import IKey

from GameObject import GameObject
from Vector import Vector

from Dependencybuillder import Dependency

key :IKey = Dependency[IKey]()

class TestObject(GameObject):
    def __init__(self):
        super().__init__()
        
        self.vec = Vector(0,0)
    
    def set_data(self, data):
        super().set_data(data)
        
        if "vec" in data:
            self.vec = Vector(data["vec"][0], data["vec"][1])
       
    def update(self):
        super().update()
        self.vec = Vector(0,0)
        
        if(key.get_key_repeat(K_a)):
            self.vec += Vector(-5,0)
        if(key.get_key_repeat(K_d)):
            self.vec += Vector(5,0)
        if(key.get_key_repeat(K_w)):
            self.vec += Vector(0,-5)
        if(key.get_key_repeat(K_s)):
            self.vec += Vector(0,5)
            
        self._position += self.vec
            
            