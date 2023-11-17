import pygame
from pygame import locals
import os

os.chdir("..")

from GameObject import GameObject
from Vector import Vector

class Machine(GameObject):
    def __init__(self, **kwargs):
        super().__init__()
