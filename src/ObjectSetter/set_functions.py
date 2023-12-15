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
def make_obj_from_data(data: dict[str, Any], groups: IGroups) -> IGameObject:

        obj_type: type[IGameObject]
    
        if(data["class"] == ""):
            obj_type = GameObject
        else:
            obj_type = eval(f"{data['use']}.{data['class']}.{data['class']}")
            
        obj = obj_type(
            Dependency[IGroups](),
            Dependency[IDrawer](),
            Dependency[IKey](),
            Dependency[ISceneLoader](),
            Dependency[IObjectSetter]()
        )
        
        obj.set_data(data)
        
        single: ISingleGroup = Dependency[ISingleGroup]()
        single.main = obj
    
        if "parent" in data:
            parent: ISingleGroup = groups.get_component_by_name(data["parent"])
            single.parent = parent
    
        groups.add_component(single)
            
        return obj

#GameObjectを追加する処理
def add_obj(data: dict, groups: IGroups, drawer: IDrawer):
    obj: IGameObject = make_obj_from_data(data, groups)
    drawer.add(obj)
    

#グループを追加する処理
#後々作る
def add_group(data: dict, groups: IGroups, drawer: IDrawer):
    pass