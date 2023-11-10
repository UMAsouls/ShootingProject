import pygame
from pygame import locals
import os

os.chdir("..")

from GameObject import GameObject
from .Bullet import Bullet

class Bullets(pygame.sprite.LayeredDirty):
    def __init__(self):
        super().__init__()
        
        


def Start(gm):
    pass