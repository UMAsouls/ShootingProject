import pygame
from pygame import locals
import os

os.chdir("..")

from GameObject import GameObject
from Vector import Vector

class TestObject(GameObject):
    def __init__(self):
        super().__init__()
        
        self.vec = Vector(1,1)
        self.dirty = 2
    
    def set_data(self, data):
        super().set_data(data)
        
        if "vec" in data:
            self.vec = Vector(data["vec"][0], data["vec"][1])
       
    def update(self):
        super().update()
        self._position += self.vec
    