import pygame
from pygame import locals
import os

from pygameEasy.GameObject import GameObject
from pygameEasy.ObjectGroup import ObjectGroup
from .Text import Text

class UI(ObjectGroup):
    def __init__(self):
        super().__init__()
        
        