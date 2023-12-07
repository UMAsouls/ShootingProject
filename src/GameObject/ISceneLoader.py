import abc
from typing import List,Dict


class ISceneLoader(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def __init__(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def scene_load(self, path: str) -> None:
        raise NotImplementedError()