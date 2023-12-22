import pygame
from pygame.locals import *
import os
import copy

from GameObject import GameObject
from .TestBullet import TestBullet
from Vector import Vector

class TestBase(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
    def update(self):
        super().update()
        