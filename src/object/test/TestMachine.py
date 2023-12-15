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


    def shoot(self):
        bullet: TestBullet  = self._obj_setter.make_obj(self.ball)
        bullet.position = self.position
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
            
        if(self._key.get_key_down("q")):
            self.shoot()
            
        self._position += self.vel
            