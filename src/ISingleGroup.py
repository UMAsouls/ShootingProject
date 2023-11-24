import abc

from IGameObject import IGameObject

from ObjectGroup import ObjectGroup

class ISingleGroup(ObjectGroup, metaclass=abc.ABCMeta):
    
    def __init__(self) -> None:
        raise NotImplementedError
    
    def set_main(self, obj:IGameObject) -> None:
        raise NotImplementedError
    
    def get_main(self) -> IGameObject:
        raise NotImplementedError