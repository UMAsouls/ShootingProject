import pygame
import abc

from . import IGameObject

class ISingleGroup(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        pass
    
    @property
    @abc.abstractclassmethod
    def main(self) -> IGameObject:
        raise NotImplementedError()