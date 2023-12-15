import pygame
import abc

from typing import Any

class IGameObject(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def set_data(self, data: dict[str, Any]) -> None:
        pass
    
