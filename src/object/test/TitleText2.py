import pygame
from pygame.locals import *
import os

from GameObject import TextObject
from Vector import Vector

class TitleText1(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
    def update(self):
        super().update()