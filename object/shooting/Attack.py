import pygame
from pygame.locals import *
import os
import copy

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector
from .Bullet import Bullet

class Attack(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(0,0)
        self.interval = 0

        self.ball = data["ball_data"]
        self.speed = data["speed"]
        
        self.change_pivot("center")
        
        self.sound = self._music.get_sound("shot.mp3")
        
        size = pygame.display.get_surface().get_size()
        
        self.position = [size[0]/2, size[1]*3//10]
        
        self.angle = 180
        
        self._stop:bool = False


    def shoot(self , k):
        bullet: Bullet  = self._obj_setter.make_obj(self.ball)
        bullet.position = self.position
        bullet.mode = k
        self._drawer.add(bullet)
        self._music.play_effect(self.sound)
        self.interval = 0
        
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
        
        if(self._key.get_key_repeat("a")):
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("d")):
            self.vel += Vector(self.speed,0)
        if(self._key.get_key_repeat("w")):
            self.vel += Vector(0,-1*self.speed)
        if(self._key.get_key_repeat("s")):
            self.vel += Vector(0,self.speed)

        if self.interval == 25:
            if(self._key.get_key_down("c")):
                self.shoot(1)

            if(self._key.get_key_down("b")):
                self.shoot(2)

            if(self._key.get_key_down("v")):
                self.shoot(3)

            if(self._key.get_key_down("n")):
                self.shoot(4)

        else:
            self.interval += 1
           
        self.position += self.vel