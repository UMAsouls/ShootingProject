import pygame
from pygame import locals
import os

os.chdir("..")

from GameObject import GameObject
from .Edge import Edge

class Field(pygame.sprite.LayeredDirty):
    def __init__(self):
        super().__init__()
        
        


def Start(gm):
    pass