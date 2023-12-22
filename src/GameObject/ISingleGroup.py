import abc

from pygame.sprite import Group

from . import IGameObject
from Vector import Vector

class ISingleGroup(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def main(self) -> IGameObject:
        pass
    
    @main.setter
    @abc.abstractclassmethod
    def main(self, value: "ISingleGroup") -> None:
        pass
    
    @property
    @abc.abstractclassmethod
    def parent(self) -> "ISingleGroup":
        pass
    
    @property
    @abc.abstractclassmethod
    def root(self) -> "ISingleGroup":
        pass
    
    @property
    @abc.abstractclassmethod
    def position(self) -> Vector:
        pass
    
    @abc.abstractclassmethod
    def position_set(self) -> None:
        pass
    
    