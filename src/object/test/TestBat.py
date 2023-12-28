import pygame
from pygame import locals
import os
import math

from GameObject import GameObject
from .TestBullet import TestBullet
from Vector import Vector

class TestBat(GameObject):

    def hit(self, obj: TestBullet):
        obj.set_velocity(10,-90)

    def set_data(self, data):
        super().set_data(data)

        if "speed" in data:
            self.speed = data["speed"]

        self.size = [180,180]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.copy = self.image.copy()
        self.visible = False
        
        self.change_pivot("center")
        self.radius = 150
        self.position = [100,50]    #親positionとの相対位置
        
    def on_collide(self, obj: GameObject):
        if isinstance(obj, TestBullet):
            self.hit(obj)

    def rotate_bat(self):
        self.angle += 8
        if self.angle >= 188:
            self.angle = 0


    def update(self):
        super().update()

        self.vel = Vector(0,0)

        obj: GameObject = self._groups.get_single_by_name("test")

        #self.position = obj.rect.center

        if ((self._key.get_key_repeat("b"))):
            self.visible = True
            self.rotate_bat()
            
        if self._key.get_key_up("b"):
            self.visible = False
            self.angle = -8
        
        self.position = Vector(
            self.radius*math.cos(math.radians(self.angle)),
            -1*self.radius*math.sin(math.radians(self.angle))
        )

            
