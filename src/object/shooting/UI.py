import pygame
from pygame import locals
import os

os.chdir("../..")

from GameObject import GameObject
from ObjectGroup import ObjectGroup
from .Text import Text

class UI(ObjectGroup):
    def __init__(self):
        super().__init__()
        
        