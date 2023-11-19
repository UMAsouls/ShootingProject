from typing import Any
import pygame
from pygame.locals import *
import os
import sys
import abc

from Vector import Vector
from IGameObject import IGameObject
from IObjectGroup import IObjectGroup

from Drawer import Drawer

#ピボット（描写位置)
pivots = {
    "topleft":0, "top":1, "topright":2,
    "left":3, "center":4, "right":5,
    "bottomleft":6, "bottom":7, "bottomright":8
    }

#__init__のときの引数の初期値
mem = {
    "path" : "",
    "pos": Vector(0,0),
    "name" : "",
    "tag": ""
}

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path

#全てのオブジェクトの基礎
class GameObject(pygame.sprite.DirtySprite, IGameObject):
    #コンストラクタ   
    def __init__(self):
        super().__init__()
        self.image :pygame.Surface = pygame.Surface([0,0])
        self.rect :pygame.Rect = self.image.get_rect()
        
        self._position :Vector = ""
        self.__pivot :int = 0
        self._name :str = ""
        self._tag :str = ""
        
        self._moving = True
        
        self.visible :bool = True
        self.layer :int = 5
        self.dirty :int = 2
        
        Drawer.add(self)
    
    #image,rectに違う型のものを入れない
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "image" and not type(__value) is pygame.Surface:
            print("error: Do not set other value type to image")
            pygame.quit()
            sys.exit()
        elif __name == "rect" and not type(__value) is pygame.Rect:
            print("error: Do not set other value type to rect")
            pygame.quit()
            sys.exit()
        else:
            super().__setattr__(__name, __value)
            
            
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) ->None:
        self._name = name
        
        
    @property
    def moving(self) -> bool:
        return self._moving
    
    @moving.setter
    def moving(self, value) -> None:
        self._moving = value
    
    #描写位置を変える
    def change_pivot(self, piv):
        if(type(piv) is int):
            self.__pivot = piv % 9
        elif(piv in pivots):
            self.__pivot = pivots[piv]
        else:
            print(f"error: given centence {piv} isn't contained in pivots")
    
    #更新処理  
    def update(self):
        super().update()
        
        if not self.visible:
            return
        
        if(self.__pivot == 0):
            self.rect.topleft = self._position.change2list()
        elif(self.__pivot == 1):
            self.rect.top = self._position.change2list()
        elif(self.__pivot == 2):
            self.rect.topright = self._position.change2list()
        elif(self.__pivot == 3):
            self.rect.left = self._position.change2list()
        elif(self.__pivot == 4):
            self.rect.center = self._position.change2list()
        elif(self.__pivot == 5):
            self.rect.right = self._position.change2list()
        elif(self.__pivot == 6):
            self.rect.bottomleft = self._position.change2list()
        elif(self.__pivot == 7):
            self.rect.bottom = self._position.change2list()
        elif(self.__pivot == 8):
            self.rect.bottomright = self._position.change2list()
        else:
            pass
        
    def add(self, *groups: IObjectGroup):
        super().add(*groups)
            
            
    def set_data(self, data):
        path :str = get_parent_path(1)
        self.image = pygame.image.load(path + f"/image/{data['path']}")
        self.rect = self.image.get_rect()
        self.name = data["name"]
        self.tag = data["tag"]
        self._position = Vector(data["pos"][0], data["pos"][1])