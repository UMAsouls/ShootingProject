import pygame
from pygame import locals
import os

from GameObject import GameObject
from Vector import Vector

class Bullet(GameObject):
    def __init__(self, **kwargs):
        super().__init__()
        
        self.vel = Vector(1,1)
        
    def update(self):
        pass