import pygame

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector
from pygameEasy.ObjectGroup import ObjectGroup

class Bar1(GameObject):
    def set_data(self, data):
        super().set_data(data)
        
        self.ratio = 1.0
        self.max_size = self.size
        
        size = pygame.display.get_surface().get_size()
        
        self.position = [100, size[1]*8/10]
        
    def set_ratio(self, r):
        if 0 <= r <= 1:
            self.ratio = r
        
    def update(self):
        super().update()
        
        self.size = [self.max_size.x*self.ratio, self.max_size.y]
        
        