import pygame
import abc

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()