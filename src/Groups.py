import pygame
import injector

from IGroups import IGroups
from IObjectGroup import IObjectGroup
from IGameObject import IGameObject

@injector.singleton
class Groups(IGroups):
    def __init__(self) -> None:
        self._groups = {}
        
    def get_group(self, name:str) -> IObjectGroup:
        return self._groups[name]
    
    def add_group(self, group: IObjectGroup) -> IObjectGroup:
        if not group.name in self._groups:
            self._groups[group.name] = group
        else:
            print("\nERROR: Don't put same name object or group\n")
            raise AttributeError()
        
    def get_single(self, name:str) -> IGameObject:
        single: IObjectGroup = self._groups[name]
        return single.sprites()[0]