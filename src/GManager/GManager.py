import pygame
from pygame.locals import *
import sys
import os
import injector

from . import IDrawer
from . import IKey
from . import IGroups
from . import ISceneLoader
from . import IObjectGroup
from . import IGameObject
from . import ISingleGroup
from . import IObjectSetter

from Vector import Vector
    

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path


#ゲームの統括クラス
class GManager:
    def __init__(self, groups: IGroups, key: IKey, drawer: IDrawer, scene_loader: ISceneLoader, object_setter: IObjectSetter) -> None:
        pygame.init()
        #ゲーム画面
        self.screen = pygame.display.set_mode([1920,1080], HWSURFACE)
        self.groups: IGroups = groups
        self.key: IKey = key
        self.drawer: IDrawer = drawer
        self.scene_loader : ISceneLoader = scene_loader
        self.object_setter : IObjectSetter = object_setter
        
        self.set_data: function = None
        
    #関数の取得
    def set_func(self, set_data) -> None:
        self.set_data = set_data
        
    def reload(self) -> None:
        self.groups.init()
        self.drawer.init()
    
        
    #ゲームの開始処理
    def start(self) -> None:
        self.drawer.draw(self.screen)
        pygame.display.update()
    
    #ゲームの更新処理
    def update(self) -> None:
        self.drawer.update()
        self.drawer.draw(self.screen)
        
        self.key.update()
        
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                sys.exit()
                
            if(event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                self.key.key_down_update(event)
                
            if(event.type == KEYUP):
                self.key.key_up_update(event)
    
    #メインループ    
    def MainLoop(self):
        self.scene_loader.end_scene
        while True:
            self.object_setter.set_data(self.scene_loader.scene_data)
            self.start()
            while True:
                self.update()
                if self.scene_loader.end_scene:
                    self.reload()
                    break
            
        
            
        
        
        
        
if __name__ == "__main__" :
    pass