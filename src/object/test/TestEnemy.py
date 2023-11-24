import pygame
from pygame import locals
import os

os.chdir("../..")

from GameObject import GameObject
from Vector import Vector

class TestEnemy(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
       
        self.image = pygame.transform.rotate(self.image,180)
        
        self.time = 1
        
    def update(self):
        super().update()

        self.vel = 0