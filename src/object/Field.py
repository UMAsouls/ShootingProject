import pygame
from pygame import locals
import os

os.chdir("..")

from GameObject import GameObject
from ObjectGroup import ObjectGroup
from .Edge import Edge

class Field(ObjectGroup):
    def __init__(self):
        super().__init__()
        
        
