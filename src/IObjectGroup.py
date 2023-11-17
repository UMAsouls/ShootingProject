import abc

from IGameObject import IGameObject

class IObjectGroup(metaclass = abc.ABCMeta):
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
    def is_single(self) -> bool:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def set_single(self, obj: IGameObject):
        raise NotImplementedError
    
    @abc.abstractclassmethod
    def set_data(self, data: list):
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def add(self, *sprites) -> None:
        raise NotImplementedError()