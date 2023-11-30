import pygame
import abc

from .IObjectGroup import IObjectGroup
from .IGameobject import IGameObject

class ISingleGroup(IObjectGroup):
    @abc.abstractclassmethod
    def set_main(self, obj: IGameObject) -> None:
        raise NotImplementedError()