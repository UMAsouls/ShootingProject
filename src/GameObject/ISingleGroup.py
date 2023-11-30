import abc

from . import IGameObject

from .IObjectGroup import IObjectGroup

class ISingleGroup(IObjectGroup):
    @abc.abstractclassmethod
    def get_main(self) -> IGameObject:
        raise NotImplementedError