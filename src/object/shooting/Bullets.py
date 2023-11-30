import pygame
from pygame import locals
import os

from GameObject import GameObject
from ObjectGroup import ObjectGroup
from .Bullet import Bullet

class Bullets(ObjectGroup):
    def __init__(self):
        super().__init__()
        