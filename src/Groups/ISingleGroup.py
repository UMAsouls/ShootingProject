import pygame
import abc

from . import IObjectGroup
from . import IGameObject

class ISingleGroup(IObjectGroup):
    @abc.abstractclassmethod
    def get_main(self) -> IGameObject:
        raise NotImplementedError()