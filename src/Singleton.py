import abc
from typing import Any


class Singleton(object, metaclass = abc.ABCMeta):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
            
        return cls._instance
    
    @abc.abstractclassmethod
    def init(self, *args, **kwargs) -> None:
        pass
    
    def __init__(self, *args, **kwargs) -> bool:
        if not hasattr(self, "__isinited"):
            self.init(*args, **kwargs)
            self.__isinited = True
        
            
            