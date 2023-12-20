from typing import Any
import pygame
from pygame.locals import *
import os
import sys
import injector

from Vector import Vector

from . import IObjectGroup
from . import ISingleGroup
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
from ObjectSetter import IGameObject as I5

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
class GameObject(I0,I1,I2,I3,I4,I5):
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
        
        self._position :Vector = Vector(0,0)
        self.__angle :int = 0
        self.__size :Vector = Vector(0,0)
        self.__pivot :int = 0
        self._name :str = ""
        self._tag :str = ""
        
        self._base_image :pygame.Surface = pygame.Surface([0,0])
        
        self._component: ISingleGroup = None
        
        self._moving: bool = True
        
        #シングルトン
        #様々な要素にアクセス可能
        self._groups :IGroups = groups
        self._drawer :IDrawer = drawer
        self._key :IKey = key
        self._scene_loader :ISceneLoader = scene_loader
        self._obj_setter :IObjectSetter = object_setter
        
        #元々の要素の初期化
        self.visible :bool = True
        self.layer :int = 5
        self.dirty :int = 2
        self.image :pygame.Surface = self._base_image.copy()
        self.rect :pygame.Rect = self.image.get_rect()
    
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
        elif __name == "rect":
            super().__setattr__(__name, __value)
            #self.__rect_set()
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
        return self._position.__copy__()
    
    #positionが変わったらそれに合わせてrectも変化する
    @position.setter
    def position(self, pos: Vector | list[int]) -> None:
        if(isinstance(pos,Vector)):
            pos = pos.change2list()
            
        self._position.x = pos[0]
        self._position.y = pos[1]    
        
        self.__rect_set()
        
    @property
    def moving(self) -> bool:
        return self._moving
    
    @moving.setter
    def moving(self, value) -> None:
        self._moving = value
        
    @property
    def component(self) -> ISingleGroup:
        return self._component
    
    @component.setter
    def component(self, value: ISingleGroup) -> None:
        self._component = value
        if(self._component.main != self):
            self._component.main = self
            
    
    @property
    def angle(self) -> int:
        return self.__angle
    
    @angle.setter
    def angle(self, angle: int) -> None:
        self.__angle = angle % 360
        
        image: pygame.Surface = pygame.transform.scale(self._base_image,self.__size.change2list())
        image = pygame.transform.rotozoom(image, self.__angle, 1)
        rect = image.get_rect()
        rect.size = self.size.change2list()
        rect.center = [image.get_width()//2, image.get_height()//2]
        self.image = image.subsurface(rect)
        
        self.rect = self.image.get_rect()
        self.__rect_set()
        
    @property
    def size(self) -> Vector:
        return self.__size.__copy__()
    
    @size.setter
    def size(self, size: Vector | list[int]) -> None:
        if isinstance(size,Vector): size = Vector.change2list
        self.__size.x = size[0]
        self.__size.y = size[1]
        
        image: pygame.Surface = pygame.transform.scale(self._base_image,self.__size.change2list())
        image = pygame.transform.rotozoom(image, self.__angle, 1)
        rect = image.get_rect()
        rect.size = self.size.change2list()
        rect.center = [image.get_width()//2, image.get_height()//2]
        self.image = image.subsurface(rect)
        
        self.rect = self.image.get_rect()
        self.__rect_set()
        
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
    
    #positionをrectにセット
    def __rect_set(self):
        size = self.rect.size
        if(self.__pivot == 0):
            self.rect.topleft = self._position.change2list()
        elif(self.__pivot == 1):
            self.rect.midtop = self._position.change2list()
        elif(self.__pivot == 2):
            self.rect.topright = self._position.change2list()
        elif(self.__pivot == 3):
            self.rect.midleft = self._position.change2list()
        elif(self.__pivot == 4):
            self.rect.center = self._position.change2list()
        elif(self.__pivot == 5):
            self.rect.midright = self._position.change2list()
        elif(self.__pivot == 6):
            self.rect.bottomleft = self._position.change2list()
        elif(self.__pivot == 7):
            self.rect.midbottom = self._position.change2list()
        elif(self.__pivot == 8):
            self.rect.bottomright = self._position.change2list()
        else:
            pass
        
        self.rect.size = size
    
    #更新処理  
    def update(self):
        pygame.sprite.DirtySprite.update(self)
        
        if not self.visible:
            return
        
        self.__rect_set()
        
        collides = pygame.sprite.spritecollide(self, self._drawer, False)
        
        for i in collides:
            self.on_collide(i)
            
            
    #jsonデータのセット       
    def set_data(self, data):
        self._base_image = pygame.image.load(PROJECT_PATH + f"/image/{data['path']}")
        self.image = self._base_image.subsurface(self._base_image.get_rect())
        self.rect = self.image.get_rect()
        self.__size = Vector(self.rect.width,self.rect.height)
        self.__angle = 0
        self.name = data["name"]
        self.tag = data["tag"]
        self._position = Vector(data["pos"][0], data["pos"][1])
        self.layer = data["layer"]

