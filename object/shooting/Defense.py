import pygame
from pygame.locals import *
import os
import copy

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector
from .Bullet import Bullet

class Defense(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(0,0)
        self.speed = data["speed"]
        
        self.change_pivot("center")
        
        size = pygame.display.get_surface().get_size()
        
        self.position = [size[0]/2, size[1]*7//10]
        
        self.pos_lim = size[1] * 3 / 5
        
        self._stop:bool = False
        
    @property
    def stop(self) -> bool:
        return self._stop
    
    @stop.setter
    def stop(self, v:bool) -> None:
        self._stop = v
        
    
        
    def update(self):
        super().update()
        self.vel = Vector(0,0)
        
        if self._stop:
            return
        
        if(self._key.get_key_repeat("j")):
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("l")):
            self.vel += Vector(self.speed,0)
        if self._key.get_key_repeat("i") and self.position.y >= self.pos_lim:
            self.vel += Vector(0,-1*self.speed)
        if self._key.get_key_repeat("k") :
            self.vel += Vector(0,self.speed)
           
        self.position += self.vel