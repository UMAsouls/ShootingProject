import pygame


from .TestText import TestText

from ObjectGroup import ObjectGroup

class TestGroup(ObjectGroup):
    def set_data(self, data):
        super().set_data(data)
        
        self.objects = self.sprites()
        
    def update(self):
        super().update()
        
        pos = self.objects[0].position.change2list()
        
        text: TestText= self.objects[1]
        
        text.pos_x = pos[0]
        text.pos_y = pos[1]
        
        
        
        