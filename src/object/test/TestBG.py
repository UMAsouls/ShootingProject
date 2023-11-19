import pygame
from pygame import locals
import os

os.chdir("../..")

from IGroups import IGroups

from GameObject import GameObject
from Vector import Vector

from Dependencybuillder import Dependency
from Drawer import Drawer

groups : IGroups = Dependency[IGroups]()

class TestBG(GameObject):
    def __init__(self):
        super().__init__()
        
        Drawer.objects.change_layer(self, 0)
        
        self.time = 0
        
    def update(self):
        super().update()
        if(self.time < 0):
            self.moving = False
        else:
            self.time -= 1
        test_sp : GameObject = groups.get_single("test")
        
        #print(test_sp.name)
    