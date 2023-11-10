import pygame
from pygame import locals
import os

os.chdir("..")

from GameObject import GameObject

class Bullet(GameObject):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        
        


def Start(gm):
    pass