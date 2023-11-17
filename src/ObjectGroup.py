import pygame

from IObjectGroup import IObjectGroup
from IGameObject import IGameObject

from Drawer import Drawer

class ObjectGroup(pygame.sprite.LayeredDirty, IObjectGroup):
    def __init__(self) -> None:
        super().__init__()
        
        self._name = ""
        self._dict = {}
        self._is_single = False
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, n:str) -> None:
        self._name = n
        
    @property
    def dict(self) -> dict:
        return self._dict
    
    def set_dict(self, n:str, v:int) -> None:
        self._dict[n] = v
        
    @property
    def is_single(self) -> bool:
        return self._is_single
        
        
    def set_single(self, obj: IGameObject):
        self.name = obj.name
        self.add(obj)
        self._is_single = True
        
        
    def set_data(self, data: list) -> None:
        self._name = data["name"]
        self.add_group(self)
    
    def add(self, *sprites: IGameObject):
        super().add(*sprites)
        for i in sprites:
            if i.name in self._dict:
                print("error: don't add same name objects")
                raise Exception
                
            self._dict[i.name] = len(self.sprites())