import os
import pygame
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from GManager import GManager

from GManager import IGameObject
from GManager import IDrawer
from GManager import IGroups
from GManager import IKey
from GManager import ISceneLoader
from GManager import IObjectGroup
from GManager import ISingleGroup
from GManager import IObjectSetter

from DependencyMaker import Dependency

from Drawer import Drawer


for i in os.listdir("object"):
    if i[0] == "_" or i[0] == ".": 
        continue
    exec(f"from object" + " import " + f"{i}")

from GameObject.Objectbuillder import Dependencybuillder

def make_obj_from_str(c_name: str) -> IGameObject:
        if(c_name == "."):
            c_name = "GameObject"
        else:
            path = c_name.split(".")
            c_name = f"{path[0]}.{path[1]}.{path[1]}"
            
        obj = eval(f"{c_name}")(
            Dependency[IGroups](),
            Dependency[IDrawer](),
            Dependency[IKey](),
            Dependency[ISceneLoader](),
            Dependency[IObjectSetter]()
        )
            
        return obj

#GameObjectを追加する処理
def add_obj(data: dict, groups: IGroups, drawer: IDrawer):
    obj: IGameObject = make_obj_from_str(f"{data['use']}.{data['class']}")
    obj.set_data(data)
    drawer.add(obj)
    group: ISingleGroup = Dependency[ISingleGroup]()
    group.set_main(obj)
    
    groups.add_group(group)

#グループを追加する処理
#後々作る
def add_group(data: dict, groups: IGroups, drawer: IDrawer):
    pass



def main():
    obj_setter: IObjectSetter = Dependency[IObjectSetter]()
    obj_setter.set_func(add_obj, add_group)
    obj_setter.set_dependency(Dependency[IGroups]() ,Dependency[IDrawer]())
    
    gm = GManager(
        groups=Dependency[IGroups](),
        key=Dependency[IKey](),
        drawer=Dependency[IDrawer](),
        scene_loader=Dependency[ISceneLoader](),
        object_setter=Dependency[IObjectSetter]()
        )
    #gm.set_func(set_data)
    gm.scene_loader.scene_load("test2.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()