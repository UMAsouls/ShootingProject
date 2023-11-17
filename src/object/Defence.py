import pygame
from pygame import locals
import os

from .Machine import Machine
from .Bullet import Bullet

class Defence(Machine):
    def __init__(self, **kwargs):
        super().__init__()
        
        