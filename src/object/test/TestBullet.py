import pygame
from pygame import locals
import os
import math

from GameObject import GameObject
from Vector import Vector

class TestBullet(GameObject):
    def set_data(self, data):
        super().set_data(data)

        self.t = 0

    def set_position(self, x, y):
        self._position = (x, y)

    def set_velocity(self, speed, angle):
        x = speed * math.cos(math.radians(angle))
        y = speed * math.sin(math.radians(angle))
        self.vel = Vector(x,y)

    def set_velocity_street(self):
        self.set_velocity(20, 90)

    def set_velocity_crave(self, gravity):
        self.set_velocity(13,40)
        vx0 = self.vel.x
        vy0 = self.vel.y
        
        dx_dt = -gravity * self.t + vx0
        dy_dt = vy0

        self.vel = Vector(dx_dt, dy_dt)
        self.t += 0.1



           
    def update(self):
        super().update()
        self.set_velocity_crave(1.8)
        self._position += self.vel
