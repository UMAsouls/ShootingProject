import pygame
from pygame.locals import *
import os

os.chdir("../..")

from GameObject import GameObject
from Vector import Vector

class TestBat(GameObject):

    def set_data(self, data):

        super().set_data(data)
        self.visible = False

        if "speed" in data:
            self.speed = data["speed"]

    def update(self):
        super().update()
        self.vel = Vector(0,0)
        self.image = pygame.transform.scale(self.image,(180,120))

        if(self._key.get_key_repeat("a")):
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("d")):
            self.vel += Vector(self.speed,0)
        if(self._key.get_key_repeat("w")):
            self.vel += Vector(0,-1*self.speed)
        if(self._key.get_key_repeat("s")):
            self.vel += Vector(0,self.speed)
        if ((self._key.get_key_repeat("b"))):
            self.visible = True
        self._position += self.vel
            
        pygame.sprite.collide_rect(self.position,)
