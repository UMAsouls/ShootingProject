from typing import Any
import pygame
from pygame.locals import *
import os
import sys
import injector

from Vector import Vector

from . import IObjectGroup
from . import IGroups
from . import IDrawer
from . import IKey
from . import ISceneLoader
from . import IObjectSetter

from Drawer import IGameObject as I0
from GManager import IGameObject as I1
from Groups import IGameObject as I2
from ObjectGroup import IGameObject as I3
from . import IGameObject as I4

#ピボット（描写位置)
PIVOTS = {
    "topleft":0, "top":1, "topright":2,
    "left":3, "center":4, "right":5,
    "bottomleft":6, "bottom":7, "bottomright":8
    }

PROJECT_PATH = os.path.dirname(os.getcwd())

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path

#全てのオブジェクトの基礎
class GameObject(I0,I1,I2,I3,I4):
    #コンストラクタ
    def __init__(
        self,
        groups: IGroups,
        drawer: IDrawer, 
        key: IKey, 
        scene_loader: ISceneLoader,
        object_setter: IObjectSetter
        ):
        
        super().__init__()
        self.image :pygame.Surface = pygame.Surface([0,0])
        self.rect :pygame.Rect = self.image.get_rect()
        
        self._position :Vector = None
        self.__pivot :int = 0
        self._name :str = ""
        self._tag :str = ""
        
        self._moving: bool = True
        
        #シングルトン
        #様々な要素にアクセス可能
        self._groups :IGroups = groups
        self._drawer :IDrawer = drawer
        self._key :IKey = key
        self._scene_loader :ISceneLoader = scene_loader
        self._obj_setter :IObjectSetter = object_setter
        
        self.visible :bool = True
        self.layer :int = 5
        self.dirty :int = 2
    
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
            
    #ここからセッター、ゲッター       
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) ->None:
        self._name = name
        
    @property
    def position(self) -> Vector:
        return self._position
    
    @position.setter
    def position(self, pos: Vector) -> None:
        self._position = pos
        
        
    @property
    def moving(self) -> bool:
        return self._moving
    
    @moving.setter
    def moving(self, value) -> None:
        self._moving = value
        
    #ここまでセッター、ゲッター
    
    #描写位置を変える
    def change_pivot(self, piv):
        if(type(piv) is int):
            self.__pivot = piv % 9
        elif(piv in PIVOTS):
            self.__pivot = PIVOTS[piv]
        else:
            print(f"error: given centence {piv} isn't contained in pivots")
            
    def on_collide(self, obj: "GameObject"):
        pass
    
    #更新処理  
    def update(self):
        pygame.sprite.DirtySprite.update(self)
        
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
        
        collides = pygame.sprite.spritecollide(self, self._drawer, False)
        
        for i in collides:
            self.on_collide(i)
            
            
    #jsonデータのセット       
    def set_data(self, data):
        self.image = pygame.image.load(PROJECT_PATH + f"/image/{data['path']}")
        self.rect = self.image.get_rect()
        self.name = data["name"]
        self.tag = data["tag"]
        self._position = Vector(data["pos"][0], data["pos"][1])
        self.layer = data["layer"]


from DependencyMaker import DependencyMaker

from Groups import Groups
from Key import Key
from Drawer import Drawer
from SceneLoader import SceneLoader

#DIコンテナ
class Dependencybuillder(DependencyMaker):
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #IGameObjectにGameObjectを紐づけ
        binder.bind(I0, to=GameObject)
        binder.bind(I1, to=GameObject)
        binder.bind(I2, to=GameObject)
        binder.bind(I3, to=GameObject)
        binder.bind(I4, to=GameObject)
        #
        binder.bind(IGroups, to=Groups)
        #
        binder.bind(IKey, to=Key)
        #
        binder.bind(IDrawer, to=Drawer)
        #
        binder.bind(ISceneLoader, to=SceneLoader)
        
Dependency = Dependencybuillder()
