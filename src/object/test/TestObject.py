import pygame
from pygame.locals import *
import os

from GameObject import GameObject
from Vector import Vector

class TestObject(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(0,0)
        
        if "speed" in data:
            self.speed = data["speed"]
       
    def update(self):
        super().update()
        self.vel = Vector(0,0)
        
        if(self._key.get_key_repeat("j")):
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("l")):
            self.vel += Vector(self.speed,0)
        if(self._key.get_key_repeat("i")):
            self.vel += Vector(0,-1*self.speed)
        if(self._key.get_key_repeat("k")):
            self.vel += Vector(0,self.speed)
            
        self._position += self.vel
            