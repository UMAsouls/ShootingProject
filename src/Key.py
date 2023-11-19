import pygame
from pygame.locals import *
import injector

from IKey import IKey

#全てのアルファベットのリスト
key_list = [K_a+i for i in range(26)]

@injector.singleton
class Key(IKey):
    def __init__(self):
        self._key = {}
        
        for k in key_list:
            self._key[k] = {
                "down": False,
                "repeat": False,
                "up": False
                }
            
    def get_key_down(self, key) -> bool:
        return self._key[key]["down"]
    
    def get_key_repeat(self, key) -> bool:
        return self._key[key]["repeat"]
    
    def get_key_up(self, key) -> bool:
        return self._key[key]["up"]
            
    def update(self):
        for k,v in self._key.items():
            v["down"] = False
            v["up"] = False
            self._key[k] = v
        
    def key_down_update(self, event: pygame.event.Event):
        for k in self._key:
            if(event.key == k):
                self._key[k]["down"] = True
                self._key[k]["repeat"] = True
    
    def key_up_update(self, event: pygame.event.Event):
        for k in self._key:
            if(event.key == k):
                self._key[k]["up"] = True
                self._key[k]["repeat"] = False
                        