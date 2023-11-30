from typing import Any, Iterable, List, Union
import pygame
import injector
import abc

from . import IGameObject

from GameObject import IDrawer as I0
from GManager import IDrawer as I1

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Drawer(I0,I1, Singleton):
    
    def __init__(self, *sprites: Any, **kwargs: Any) -> None:
        if not hasattr(self, "_isinit"):
            super().__init__(*sprites, **kwargs)
            self.rect_list = []
            self._isinit = True
            
    def init(self) -> None:
        del self._isinit
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
                

from DependencyMaker import DependencyMaker

class Dependencybuillder(DependencyMaker):
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #
        binder.bind(I0, to=Drawer)
        binder.bind(I1, to=Drawer)
    

Dependency = Dependencybuillder()
            
        