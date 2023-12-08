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
        visibles1: list[bool] = []
        visibles2: list[bool] = []
        obj: IGameObject = None
        for obj in self.sprites():
            #コピーじゃないと参照が共有されて変更前との差分が作れない
            rects1.append(obj.rect.copy())
            visibles1.append(obj.visible)
            
        pygame.sprite.LayeredDirty.update(self)
        
        for obj in self.sprites():
            rects2.append(obj.rect.copy())
            visibles2.append(obj.visible)
            
        for v in range(len(rects1)):
            if(v >= len(rects2)):
                self.rect_list += rects1[v:]
                break
            
            i: pygame.Rect = rects1[v]
            j: pygame.Rect = rects2[v]
            if(i.center != j.center or i.size != j.size):
                self.rect_list.append(i)
                self.rect_list.append(j)
                
            elif(visibles1[v] != visibles2[v]):
                self.rect_list.append(i)
                self.rect_list.append(j)
                
        if(len(rects1) <= len(rects2)):
            self.rect_list += rects2[v:]
            
from DependencyConfig import Config

configs = [
    Config(I0, Drawer),
    Config(I1, Drawer),
    Config(I2, Drawer)
]
            
        