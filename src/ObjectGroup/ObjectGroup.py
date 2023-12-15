import pygame
import sys
import injector
import os

from .IGameObject import IGameObject

from Groups import IObjectGroup as I0
from GameObject import IObjectGroup as I1
from GManager import IObjectGroup as I2
from ObjectSetter import IObjectGroup as I3

class ObjectGroup(I0,I1,I2,I3):
    def __init__(self) -> None:
        super().__init__()
        
        self._name: str = ""
        self._dict: dict[str, int] = {}
        self._same_names: dict[str, int] = {}
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, n:str) -> None:
        self._name = n
        
    def get_obj(self, name: str) -> IGameObject:
        return self.sprites()[self._dict[name]]
        
        
    def set_data(self, data: dict) -> None:
        self._name = data["name"]
    
    def add(self, *sprites: IGameObject):
        for i in sprites:
            if i.name in self._same_names:
                self._same_names[i.name] += 1
                i.name += f"({self._same_names[i.name]})"
            else:
                self._same_names[i.name] = 0
            
            self._dict[i.name] = len(self.sprites())    
            pygame.sprite.LayeredDirty.add(self,i)
            
            
from DependencyConfig import Config

configs = [
    Config(I0, ObjectGroup),
    Config(I1, ObjectGroup),
    Config(I2, ObjectGroup),
    Config(I3, ObjectGroup)
]
