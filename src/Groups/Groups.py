import pygame
import injector
import sys

from . import IGameObject
from . import IObjectGroup
from . import ISingleGroup

from GameObject import IGroups as I0
from GManager import IGroups as I1
from ObjectSetter import IGroups as I2

from Singleton import Singleton

@injector.singleton
class Groups(I0,I1,I2,Singleton):
    _groups = {}
    _singles = {}
    _types = {}  
    __groups_same_names: dict[str, int] = {}
    __singles_same_names: dict[str, int] = {}
                        
    def init(self) -> None:
        self._groups = {}
        self._singles = {}
        self._types = {} 
        
    def get_group_by_name(self, name:str) -> IObjectGroup:
        return self._groups[name]
    
    def add_group(self, group: IObjectGroup) -> None:
        if group.name in self._groups:
            print(self._groups, group.name)
            print("\nERROR: Don't put same name group\n")
            pygame.quit()
            sys.exit()
        
        self._groups[group.name] = group
            
    def add_component(self, single: ISingleGroup) -> None:
        if single.name in self.__singles_same_names:
            self.__singles_same_names[single.name] += 1
            single.name += f"({self.__singles_same_names[single.name]})"
        else:
            self.__singles_same_names[single.name] = 0
        
        self._singles[single.name] = single
        
        
    def get_single_by_name(self, name:str) -> IGameObject:
        single: ISingleGroup = self._singles[name]
        return single.main
    
    def get_component_by_name(self, name: str) -> ISingleGroup:
        return self._singles[name]
    
    def get_group_by_type(self) -> IObjectGroup:
        return
    
from DependencyConfig import Config

configs = [
    Config(I0, lambda: Groups.get_instance()),
    Config(I1, lambda: Groups.get_instance()),
    Config(I2, lambda: Groups.get_instance())
]