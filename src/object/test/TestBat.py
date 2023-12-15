import pygame
from pygame import locals
import os
import copy

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

        self.image = pygame.transform.scale(self.image,(180,120))
        self.rect = self.image.get_rect()
        self.visible = False

    def on_collide(self, obj: GameObject):
        if isinstance(obj, TestBullet):
            self.hit(obj)

    def rotate_bat(self):
        angle = 0
        if angle <= 90:
            angle += 9
            self.image = pygame.transform.rotate((self.image),5)
            self.rect = self.image.get_rect()


    def update(self):
        super().update()

        self.vel = Vector(0,0)

        obj: GameObject = self._groups.get_single_by_name("test")

        self.position = copy.copy(obj.position)
        self.position.x += 50

        if ((self._key.get_key_repeat("b"))):
            self.visible = True
            self.rotate_bat()

            
