import pygame
import injector
import sys
import os

from . import IGameObject
from . import IObjectGroup
from . import ISingleGroup

from GameObject import IGroups as I0
from GManager import IGroups as I1

from DependencyMaker import DependencyMaker

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Groups(I0,I1,Singleton):
    def __init__(self) -> None:
        if hasattr(self, "_isinit"):
            return
            
        self._groups = {}
        self._singles = {}
        self._types = {}
        self._isinit = True
                        
    def init(self) -> None:
        del self._isinit
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
    
    
    
class Dependencybuillder(DependencyMaker):
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #
        binder.bind(I0, to=Groups)
        binder.bind(I1, to=Groups)
        
Dependency = Dependencybuillder()