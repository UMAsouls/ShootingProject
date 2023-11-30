import pygame
import sys
import injector
import os

from . import ObjectGroup
from . import IGameObject

from Groups import ISingleGroup as I0
from GManager import ISingleGroup as I1
from GameObject import ISingleGroup as I2

print(I0,I1,I2)


from DependencyMaker import DependencyMaker


class SingleGroup(I0,I1,I2,ObjectGroup):
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
        binder.bind(I0, to=SingleGroup)
        binder.bind(I1, to=SingleGroup)
        binder.bind(I2, to=SingleGroup)
        
Dependency = Dependencybuillder()
        