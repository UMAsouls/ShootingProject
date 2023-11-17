import pygame
from pygame.locals import *
import sys
import os
import abc
import json

from IGameObject import IGameObject
from IObjectGroup import IObjectGroup
from IGroups import IGroups

from Vector import Vector

from Dependencybuillder import Dependency
from Drawer import Drawer

for i in os.listdir("object"):
    if i[0] != "_":
        exec(f"from object.{i}"[0:-3] + " import " + f"{i}"[0:-3])

os.chdir(os.path.dirname(os.path.abspath(__file__)))

groups: IGroups = Dependency[IGroups]()

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
    
    #strからobj生成
    @classmethod   
    def make_obj_from_str(cls, c_name: str):
        if(c_name == ""):
            obj = Dependency[IGameObject]()
        else:
            obj = eval(f"{c_name}()")
            
        return obj
        
    #jsonデータをセット
    #同時にそのjsonでロードされる全てをgroupsに追加  
    def set_data(self, data):
        for d in data:
            obj = self.make_obj_from_str(d["class"])               
            obj.set_data(d)
            
            if(isinstance(obj, IGameObject)):
                obj: IGameObject
                group: IObjectGroup = Dependency[IObjectGroup]()
                group.set_single(obj)
            else:
                group: IObjectGroup = obj
                for d2 in d["data"]:
                    obj: IGameObject = self.make_obj_from_str(d2["class"])
                    obj.set_data(d2)
                    group.add(obj)
                
            groups.add_group(group)
                
                
    #一つのステージロード
    def scene_load(self,path) -> None:
        path = get_parent_path(1) + "/json/" + path
        with open(path) as f:
            data = json.load(f)
            
        self.set_data(data)
    
    #ゲームの更新処理
    def update(self) -> None:
        Drawer.update()
        Drawer.draw(self.screen)
        
        #イベント処理(後で移動)
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
    
    #メインループ    
    def MainLoop(self):
        while True:
            self.update()
        
            
        
        
        
        
if __name__ == "__main__" :
    pass