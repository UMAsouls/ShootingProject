import abc

class IGameObject(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @name.setter
    @abc.abstractclassmethod
    def name(self, name: str) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def update(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def add(self, *groups) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def set_data(self, data) -> None:
        raise NotImplementedError()