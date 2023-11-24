import pygame
from pygame import locals
import os

os.chdir("..")

from IGroups import IGroups

from GameObject import GameObject
from Vector import Vector

class Machine(GameObject):
    def __init__(self):
        super().__init__()
        
    
    def set_data(self, data):
        super().set_data(data)
        
        
        
