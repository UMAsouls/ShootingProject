import abc

from pygame.sprite import LayeredDirty

from . import IGameObject

class ISingleGroup(LayeredDirty):
    @property
    @abc.abstractclassmethod
    def main(self) -> IGameObject:
        pass
    
    @main.setter
    @abc.abstractclassmethod
    def main(self, value: "ISingleGroup") -> None:
        pass
    
    