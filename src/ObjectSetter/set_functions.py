import pygame
import os
from typing import Any

from .IGameObject import IGameObject
from .ISingleGroup import ISingleGroup
from .IObjectGroup import IObjectGroup

from .IGroups import IGroups
from .IDrawer import IDrawer
from .IKey import IKey
from .ISceneLoader import ISceneLoader
from .IObjectSetter import IObjectSetter

from GameObject import GameObject

for i in os.listdir("object"):
    if i[0] == "_" or i[0] == ".": 
        continue
    exec(f"from object" + " import " + f"{i}")
    

from DependencyMaker import Dependency

#jsonデータからobjectを作る
def make_obj_from_data(data: dict[str, Any]) -> IGameObject:

        obj_type: type[IGameObject]
    
        if(data["class"] == ""):
            obj_type = GameObject
        else:
            obj_type = eval(f"{data['use']}.{data['class']}.{data['class']}")
            
        single = Dependency[ISingleGroup]()
            
        obj = obj_type(
            Dependency[IGroups](),
            Dependency[IDrawer](),
            Dependency[IKey](),
            Dependency[ISceneLoader](),
            Dependency[IObjectSetter](),
            single
        )
        
        obj.set_data(data)

        #data内で子を指定することにする
        if "kid" in data:
            for i in data["kid"]:
                kid: IGameObject = make_obj_from_data(i)
                kid.component.parent = single
            
        return obj

#GameObjectを追加する処理
def add_obj(data: dict, groups: IGroups, drawer: IDrawer):
    obj: IGameObject = make_obj_from_data(data)
    groups.add_component(obj.component)
    drawer.add(obj)
    for i in obj.component.kids:
        drawer.add(i)
    

#グループを追加する処理
#後々作る
def add_group(data: dict, groups: IGroups, drawer: IDrawer):
    pass