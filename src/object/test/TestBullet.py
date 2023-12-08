import pygame
from pygame import locals
import os
import math

from GameObject import GameObject
from Vector import Vector

class TestBullet(GameObject):
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(1,1)

    def set_velocity(self, speed, angle):
        x = speed * math.cos(math.radians(angle))
        y = speed * math.sin(math.radians(angle))
        self.vel = Vector(x,y)
        print(x,y)
    
    
        
    def update(self):
        super().update()
        self.set_velocity(10,90)

        self._position += self.vel
