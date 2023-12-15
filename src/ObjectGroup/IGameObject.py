import pygame
import abc

from .ISingleGroup import ISingleGroup

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    @abc.abstractclassmethod
    def component(self) -> ISingleGroup:
        pass
    
    @component.setter
    @abc.abstractclassmethod
    def component(self, component: ISingleGroup) -> None:
        pass