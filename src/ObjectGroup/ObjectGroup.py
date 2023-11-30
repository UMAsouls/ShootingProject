import pygame
import sys
import injector
import os

from .IGameObject import IGameObject

from Groups import IObjectGroup as I0
from GameObject import IObjectGroup as I1
from GManager import IObjectGroup as I2

class ObjectGroup(I0,I1,I2):
    def __init__(self) -> None:
        super().__init__()
        
        self._name = ""
        self._dict = {}
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, n:str) -> None:
        self._name = n
        
    @property
    def dict(self) -> dict:
        return self._dict
    
    def set_dict(self, n:str, v:int) -> None:
        self._dict[n] = v
        
        
    def set_data(self, data: dict) -> None:
        self._name = data["name"]
    
    def add(self, *sprites: IGameObject):
        pygame.sprite.LayeredDirty.add(self,*sprites)
        for i in sprites:
            if i.name in self._dict:
                print("error: don't add same name objects")
                pygame.quit()
                sys.exit()
                
            self._dict[i.name] = len(self.sprites())
            
class Dependencybuillder:
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        binder.bind(I0, to=ObjectGroup)
        binder.bind(I1, to=ObjectGroup)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    

Dependency = Dependencybuillder()