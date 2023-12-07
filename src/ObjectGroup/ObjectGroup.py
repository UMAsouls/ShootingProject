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
        
        self._name: str = ""
        self._dict: dict[str, int] = {}
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, n:str) -> None:
        self._name = n
        
    @property
    def dict(self) -> dict[str, int]:
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
            
from DependencyConfig import Config

configs = [
    Config(I0, ObjectGroup),
    Config(I1, ObjectGroup),
    Config(I2, ObjectGroup)
]
