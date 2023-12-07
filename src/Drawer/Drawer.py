from typing import Any
import pygame
import injector

from . import IGameObject

from GameObject import IDrawer as I0
from GManager import IDrawer as I1
from ObjectSetter import IDrawer as I2

@injector.singleton
class Drawer(I0,I1,I2):
    def __init__(self, *sprites: Any, **kwargs: Any) -> None:
        pygame.sprite.LayeredDirty.__init__(self,*sprites,**kwargs)
        self.rect_list: list[pygame.Rect] = []
            
            
    def init(self) -> None:
        self.__init__()

    def draw(self, screen: pygame.Surface):
        rects = pygame.sprite.LayeredDirty.draw(self,screen)
        pygame.display.update(self.rect_list)
        return rects
    
    def sprites(self) -> list:
        return super().sprites()
        
    def update(self):
        self.rect_list = []
        rects1 = []
        rects2 = []
        obj: IGameObject = None
        for obj in self.sprites():
            #コピーじゃないと参照が共有されて変更前との差分が作れない
            rects1.append(obj.rect.copy())
            
        pygame.sprite.LayeredDirty.update(self)
        
        for obj in self.sprites():
            rects2.append(obj.rect.copy())
            
        for v,i in enumerate(rects1):
            i: pygame.Rect
            j: pygame.Rect = rects2[v]
            if(i.center != j.center or i.size != j.size):
                self.rect_list.append(i)
                self.rect_list.append(j)
                

from DependencyConfig import Config

configs = [
    Config(I0, Drawer),
    Config(I1, Drawer),
    Config(I2, Drawer)
]
            
        