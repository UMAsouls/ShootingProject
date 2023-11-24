import pygame
import sys
import injector

from ISingleGroup import ISingleGroup
from IGameObject import IGameObject

from DependencyMaker import DependencyMaker
from ObjectGroup import ObjectGroup

class SingleGroup(ISingleGroup):
    def __init__(self) -> None:
        ObjectGroup.__init__(self)
        self.main: IGameObject = None
        
    def set_main(self, obj: IGameObject) -> None:
        self.add(obj)
        self.name = obj.name
        self.main = obj
        
    def get_main(self) -> IGameObject:
        return self.main
    
    
class Dependencybuillder(DependencyMaker):
    
    @classmethod
    def configure(cls, binder: injector.Binder):
        binder.bind(ISingleGroup, to=SingleGroup)
        
Dependency = Dependencybuillder()
        