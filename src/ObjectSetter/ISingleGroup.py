import pygame
import abc

from .IGameObject import IGameObject

class ISingleGroup(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    
    @property
    @abc.abstractclassmethod
    def main(self, obj: IGameObject) -> None:
        pass
    
    @property
    @abc.abstractclassmethod
    def parent(self, component: "ISingleGroup") -> None:
        pass