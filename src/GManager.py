import pygame
from pygame.locals import *
import sys
import os
import json

from IGameObject import IGameObject
from IObjectGroup import IObjectGroup
from ISingleGroup import ISingleGroup
from IGroups import IGroups
from IKey import IKey
from IDrawer import IDrawer
from ISceneLoader import ISceneLoader

import GameObject
import ObjectGroup
import SingleGroup
import Drawer
import Groups
import Key
import SceneLoader

from Objectbuillder import Dependencybuillder

from Vector import Vector

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#objectから全てimport
for i in os.listdir("object"):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if i[0] == "_" or i[0] == ".": 
        continue
    exec(f"from object" + " import " + f"{i}")
    

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path


#ゲームの統括クラス
class GManager:
    def __init__(self) -> None:
        pygame.init()
        #ゲーム画面
        self.screen = pygame.display.set_mode([1920,1080], FULLSCREEN)
        self.groups: IGroups = Groups.Dependency[IGroups]()
        self.key: IKey = Key.Dependency[IKey]()
        self.drawer: IDrawer = Drawer.Dependency[IDrawer]()
        self.scene_loader : ISceneLoader = SceneLoader.Dependency[ISceneLoader]()
    
    #strからobj生成
    @classmethod   
    def make_obj_from_str(cls, c_name: str):
        if(c_name == ""):
            dep = GameObject.Dependency
        else:
            dep = Dependencybuillder(c_name)
            
        obj = dep[IGameObject]()
            
        return obj
        
    #jsonデータをセット
    #同時にそのjsonでロードされる全てをgroupsに追加  
    def set_data(self, data):
        for d in data["obj"]:
            obj = self.make_obj_from_str(f"{data['use']}.{d['class']}")
            obj.set_data(d)
            
            if(isinstance(obj, IGameObject)):
                obj: IGameObject
                self.drawer.add(obj)
                print(self.drawer.sprites())
                group: ISingleGroup = SingleGroup.Dependency[ISingleGroup]()
                group.set_main(obj)
            else:
                group: IObjectGroup = obj
                #json内でグループ型があった際の処理（応急処置：入れ子でも対応すべきか？）
                for d2 in d["data"]:
                    obj: IGameObject = self.make_obj_from_str(f"{data['use']}.{d2['class']}")
                    obj.set_data(d2)
                    self.drawer.add(obj)
                    group.add(obj)
                
            self.groups.add_group(group)
        
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
            self.set_data(self.scene_loader.scene_data)
            self.start()
            while True:
                self.update()
                if self.scene_loader.end_scene:
                    break
            
        
            
        
        
        
        
if __name__ == "__main__" :
    pass