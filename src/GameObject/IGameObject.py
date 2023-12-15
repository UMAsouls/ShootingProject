import pygame
import abc

from Vector import Vector

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def position(self) -> Vector:
        pass
    
    @position.setter
    @abc.abstractclassmethod
    def position(self, vec: Vector) -> None:
        pass