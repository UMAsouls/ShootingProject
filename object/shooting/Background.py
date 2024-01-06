import pygame

from pygameEasy.GameObject import GameObject

class Background(GameObject):
    def set_data(self, data):
        super().set_data(data)
        
        size = pygame.display.get_surface().get_size()
        
        self.size = size
        
    def update(self):
        super().update()