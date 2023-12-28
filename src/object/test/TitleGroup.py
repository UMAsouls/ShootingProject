import pygame


from .TestText import TestText

from ObjectGroup import ObjectGroup

class TitleGroup(ObjectGroup):
    def set_data(self, data):
        super().set_data(data)
        
    def update(self):
        super().update()