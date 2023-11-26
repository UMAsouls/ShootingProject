from typing import Any, Iterable, Union
import pygame
import injector
from pygame.sprite import AbstractGroup

from IGameObject import IGameObject
from IDrawer import IDrawer

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Drawer(IDrawer, Singleton):
    
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
        
    def update(self):
        self.rect_list = []
        rects1 = []
        rects2 = []
        for i in self.sprites():
            #コピーじゃないと参照が共有されて変更前との差分が作れない
            rects1.append(i.rect.copy())
            
        pygame.sprite.LayeredDirty.update(self)
        
        for i in self.sprites():
            rects2.append(i.rect.copy())
            
        for v,i in enumerate(rects1):
            i: pygame.Rect
            j: pygame.Rect = rects2[v]
            if(i.center != j.center or i.size != j.size):
                self.rect_list.append(i)
                self.rect_list.append(j)
                
class Dependencybuillder:
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #
        binder.bind(IDrawer, to=Drawer)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    

Dependency = Dependencybuillder()
            
        