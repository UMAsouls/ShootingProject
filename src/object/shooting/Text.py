import pygame
from pygame import locals
import os

from GameObject import GameObject

class Text(GameObject):
    def __init__(self, **kwargs):
        super().__init__()
        
        