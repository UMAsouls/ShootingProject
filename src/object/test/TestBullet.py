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
        self.mode = 0

    def set_position(self, x, y):
        self._position = (x, y)

    def set_velocity(self, speed, angle):
        x = speed * math.cos(math.radians(angle))
        y = speed * math.sin(math.radians(angle))
        self.vel = Vector(x,y)
    
    #ストレート       
    def set_velocity_street(self):
        self.set_velocity(20, 90)

    #カーブ
    def set_velocity_crave(self, gravity):
        self.set_velocity(13,40)
        vx0 = self.vel.x
        vy0 = self.vel.y
        
        dx_dt = -gravity * self.t + vx0
        dy_dt = vy0

        self.vel = Vector(dx_dt, dy_dt)
        self.t += 0.1

    #逆カーブ
    def set_velocity_uncrave(self, gravity):
        self.set_velocity(13,130)
        vx0 = self.vel.x
        vy0 = self.vel.y
        
        dx_dt = gravity * self.t + vx0
        dy_dt = vy0

        self.vel = Vector(dx_dt, dy_dt)
        self.t += 0.1

    #行って戻って
    def set_velocity_goback(self, gravity):
        self.set_velocity(0,-40)
        vx0 = self.vel.x
        vy0 = self.vel.y

        dy_dt = gravity * self.t + vy0
        dx_dt = vx0 * self.t

        self.vel = Vector(dx_dt, dy_dt)
        self.t += 0.1

    #反射
    def reflect(self):
        self.vel.x = -self.vel.x
        self.vel.y = -self.vel.y
           
    def update(self):
        super().update()
        if self.mode == 1:
           self.set_velocity_street()

        elif self.mode == 2:
            self.set_velocity_crave(1.8)

        elif self.mode == 3:
            self.set_velocity_uncrave(1.8)

        elif self.mode == 4:
            self.set_velocity_goback(1.8)

        self._position += self.vel
