import pygame
import injector
import sys

from . import IGameObject
from . import IObjectGroup
from . import ISingleGroup

from GameObject import IGroups as I0
from GManager import IGroups as I1
from ObjectSetter import IGroups as I2

@injector.singleton
class Groups(I0,I1,I2):
    def __init__(self) -> None:            
        self._groups = {}
        self._singles = {}
        self._types = {}
                        
    def init(self) -> None:
        self.__init__()
        
    def get_group_by_name(self, name:str) -> IObjectGroup:
        return self._groups[name]
    
    def add_group(self, group: IObjectGroup) -> IObjectGroup:
        if group.name in self._groups:
            print(self._groups, group.name)
            print("\nERROR: Don't put same name group\n")
            pygame.quit()
            sys.exit()
        
        self._groups[group.name] = group
        if isinstance(group, ISingleGroup):
            self._singles[group.name] = group
        
        
    def get_single_by_name(self, name:str) -> IGameObject:
        single: ISingleGroup = self._singles[name]
        return single.get_main()
    
    def get_group_by_type(self) -> IObjectGroup:
        return
    
from DependencyConfig import Config

configs = [
    Config(I0, Groups),
    Config(I1, Groups),
    Config(I2, Groups)
]