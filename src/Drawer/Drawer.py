from typing import Any
import pygame
import injector
from dataclasses import dataclass

from . import IGameObject

from GameObject import IDrawer as I0
from GManager import IDrawer as I1
from ObjectSetter import IDrawer as I2

from Singleton import Singleton

@injector.singleton
class Drawer(I0,I1,I2,Singleton):
    rect_list: list[pygame.Rect] = []
    
    @classmethod    
    def get_instance(cls) -> "Drawer":
        if cls._instance == None:
            cls._instance = cls.__internal_new__()
            cls.inited: bool = False
            pygame.sprite.LayeredDirty.__init__(cls._instance)
        
        return cls._instance
        
            
            
    def init(self) -> None:
        self.rect_list = []
        pygame.sprite.LayeredDirty.__init__(self)

    def draw(self, screen: pygame.Surface):
        rects = pygame.sprite.LayeredDirty.draw(self,screen)
        #pygame.display.update(self.rect_list)
        pygame.display.flip()
        return rects
    
    def sprites(self) -> list[IGameObject]:
        return super().sprites()
    
    def __rect_list_gen(self):
        for i in self.sprites():
            if i.changed:
                yield i.rect
        
    def update(self):
        self.rect_list = []
            
        pygame.sprite.LayeredDirty.update(self)
        
        self.rect_list = list(self.__rect_list_gen())
        
        
            
from DependencyConfig import Config

configs = [
    Config(I0, lambda: Drawer.get_instance()),
    Config(I1, lambda: Drawer.get_instance()),
    Config(I2, lambda: Drawer.get_instance())
]
            
        