import abc

from IObjectGroup import IObjectGroup
from IGameObject import IGameObject

class IGroups(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def get_group(self, name:str) -> IObjectGroup:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def add_group(self, group:IObjectGroup) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def get_single(self, name:str) -> IGameObject:
        raise NotImplementedError()