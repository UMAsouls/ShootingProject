import abc
import pygame

class IGameObject(pygame.sprite.DirtySprite,metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @name.setter
    @abc.abstractclassmethod
    def name(self, name: str) -> None:
        raise NotImplementedError()
    
    @property
    @abc.abstractclassmethod
    def position(self):
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def update(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def set_data(self, data) -> None:
        raise NotImplementedError()