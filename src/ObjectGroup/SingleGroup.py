import pygame
import sys
import injector
import os

from . import ObjectGroup
from . import IGameObject

from Groups import ISingleGroup as I0
from GManager import ISingleGroup as I1
from GameObject import ISingleGroup as I2


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
    
    
from DependencyConfig import Config

configs = [
    Config(I0, SingleGroup),
    Config(I1, SingleGroup),
    Config(I2, SingleGroup)
]
        