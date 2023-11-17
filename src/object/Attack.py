import pygame
from pygame import locals
import os

from .Machine import Machine
from .Bat import Bat

class Attack(Machine):
    def __init__(self, **kwargs):
        super().__init__()
        
        