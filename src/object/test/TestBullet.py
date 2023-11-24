import pygame
from pygame import locals
import os

os.chdir("../..")

from GameObject import GameObject
from Vector import Vector

class TestBullet(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        print(self.rect.size)
        self.time = 1
        
    #ストレート
    def strate_1(self):
        self.vel = 20

        self._position.y += self.vel

    #カーブ
    def carve(self):
        t=0
        self.vel = 10
        self._position.y += self.vel
        self._position.x += -1*t
        t += 1

    def update(self):
        super().update()
        self.strate_1()

        

        #フォーク

        
        #print(test_sp.name)