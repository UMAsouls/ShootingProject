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
        self.interval: float = 1.0

        self.ball = data["ball_data"]
        self.max_speed = data["speed"]
        self.speed = data["speed"]
        
        self.change_pivot("center")
        
        self.sound = self._music.get_sound("shot.mp3")
        
        size = pygame.display.get_surface().get_size()
        
        self.position = [size[0]/2, size[1]*1//4]
        
        self.angle = 180
        
        self.pos_lim = [0, size[1]*1/15, size[0], size[1] * 1 / 3]
        
        self._stop:bool = False
        
        self.clock = pygame.time.Clock()
        
        self.late_time = 0


    def shoot(self , k):
        bullet: Bullet  = self._obj_setter.make_obj(self.ball)
        bullet.position = self.position
        bullet.mode = k
        self._drawer.add(bullet)
        self._music.play_effect(self.sound)
        self.interval = 0.0
        
    def on_collide(self, obj: GameObject):
        if isinstance(obj, Bullet):
            if obj.mode == -1:
                self.late_time = -1
            
        
    @property
    def stop(self) -> bool:
        return self._stop
    
    @stop.setter
    def stop(self, v:bool) -> None:
        self._stop = v
        
    def update(self):
        
        self.speed = self.max_speed
        self.clock.tick()
        
        super().update()
        self.vel = Vector(0,0)
        
        if self._stop:
            return
        
        self.late_time += self.clock.get_time() / 1000
        
        if self.late_time < 0:
            self.speed /= 2
        
        if(self._key.get_key_repeat("a")) and self.rect.left > self.pos_lim[0]:
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("d")) and self.rect.right < self.pos_lim[2]:
            self.vel += Vector(self.speed,0)
        if(self._key.get_key_repeat("w")) and self.rect.top > self.pos_lim[1]:
            self.vel += Vector(0,-1*self.speed)
        if(self._key.get_key_repeat("s")) and self.rect.bottom <= self.pos_lim[3]:
            self.vel += Vector(0,self.speed)

        if self.interval >= 0.8:
            if(self._key.get_key_down("x")):
                self.shoot(1)

            elif(self._key.get_key_down("v")):
                self.shoot(2)

            elif(self._key.get_key_down("c")):
                self.shoot(3)

            elif(self._key.get_key_down("b")):
                self.shoot(4)

        else:
            self.interval += self.clock.get_time() / 1000
           
        self.position += self.vel