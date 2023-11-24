import pygame
from pygame.locals import *
import injector

from IKey import IKey

#全てのアルファベットの辞書
key_dict = {pygame.key.name(K_a+i) : K_a+i for i in range(26)}

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Key(IKey, Singleton):
    def __init__(self):
        if hasattr(self, "_isinit"):
            return
        
        self._key = {}
        for k in key_dict.keys():
            self._key[k] = {
                "down": False,
                "repeat": False,
                "up": False
                }
        self._isinit = True

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
                
class Dependencybuillder:
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #IGameObjectにGameObjectを紐づけ
        binder.bind(IKey, to=Key)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    

Dependency = Dependencybuillder()
                        