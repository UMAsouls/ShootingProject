import pygame
from pygame.locals import *
import injector

from GameObject import IKey as I0
from GManager import IKey as I1
from ObjectSetter import IKey as I2

from Singleton import Singleton

#全てのアルファベットの辞書
key_dict = {pygame.key.name(K_a+i) : K_a+i for i in range(26)}

@injector.singleton
class Key(I0,I1,I2,Singleton):
    _key = {}
    for k in key_dict.keys():
        _key[k] = {
            "down": False,
            "repeat": False,
            "up": False
        }

    def get_key_down(self, key: str) -> bool:
        return self._key[key]["down"]
    
    def get_key_repeat(self, key: str) -> bool:
        return self._key[key]["repeat"]
    
    def get_key_up(self, key: str) -> bool:
        return self._key[key]["up"]
            
    def update(self):
        for k,v in self._key.items():
            v["down"] = False
            v["up"] = False
            self._key[k] = v
        
    def key_down_update(self, event: pygame.event.Event):
        for k in self._key:
            if(event.key == key_dict[k]):
                self._key[k]["down"] = True
                self._key[k]["repeat"] = True
    
    def key_up_update(self, event: pygame.event.Event):
        for k in self._key:
            if(event.key == key_dict[k]):
                self._key[k]["up"] = True
                self._key[k]["repeat"] = False
                
from DependencyConfig import Config

configs = [
    Config(I0, lambda: Key.get_instance()),
    Config(I1, lambda: Key.get_instance()),
    Config(I2, lambda: Key.get_instance())
]
                        