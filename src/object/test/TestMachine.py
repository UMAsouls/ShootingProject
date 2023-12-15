import pygame
from pygame.locals import *
import os
import copy

from GameObject import GameObject
from .TestBullet import TestBullet
from Vector import Vector

class TestMachine(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(0,0)

        self.ball = data["ball_data"]
        self.speed = data["speed"]


    def shoot(self , k):
        bullet: TestBullet  = self._obj_setter.make_obj(self.ball)
        bullet.position = self.position
        bullet.mode = k
        self._drawer.add(bullet)
        
    def update(self):
        super().update()
        self.vel = Vector(0,0)
        
        if(self._key.get_key_repeat("a")):
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("d")):
            self.vel += Vector(self.speed,0)
        if(self._key.get_key_repeat("w")):
            self.vel += Vector(0,-1*self.speed)
        if(self._key.get_key_repeat("s")):
            self.vel += Vector(0,self.speed)
            
        if(self._key.get_key_down("c")):
            self.shoot(1)

        if(self._key.get_key_down("v")):
            self.shoot(2)

        if(self._key.get_key_down("m")):
            self.shoot(3)

        if(self._key.get_key_down("n")):
            self.shoot(4)
            
        self._position += self.vel
            