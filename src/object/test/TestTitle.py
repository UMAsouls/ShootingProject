import pygame
from pygame.locals import *


from GameObject import GameObject


class TestTitle(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
    def update(self):
        super().update()