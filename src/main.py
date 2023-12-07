import os
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

from ObjectGroup.ObjectGroup import Dependency as grp_dep
from ObjectGroup.SingleGroup import Dependency as sgrp_dep
from Groups.Groups import Dependency as grps_dep
from Key.Key import Dependency as key_dep
from Drawer.Drawer import Dependency as drw_dep
from SceneLoader.SceneLoader import Dependency as scene_dep
from GameObject.GameObject import Dependency as obj_dep
from ObjectSetter.ObjectSetter import Dependency as set_dep


from GameObject.Objectbuillder import Dependencybuillder

def make_obj_from_str(c_name: str) -> IGameObject:
        if(c_name == ""):
            dep = obj_dep
        else:
            dep = Dependencybuillder(c_name)
            
        obj = dep[IGameObject]()
            
        return obj

#GameObjectを追加する処理
def add_obj(data: dict, groups: IGroups, drawer: IDrawer):
    obj: IGameObject = make_obj_from_str(f"{data['use']}.{data['class']}")
    obj.set_data(data)
    drawer.add(obj)
    group: ISingleGroup = sgrp_dep[ISingleGroup]()
    group.set_main(obj)
    
    groups.add_group(group)

#グループを追加する処理
#後々作る
def add_group(data: dict, groups: IGroups, drawer: IDrawer):
    pass



def main():
    obj_setter: IObjectSetter = set_dep[IObjectSetter]()
    obj_setter.set_func(add_obj, add_group)
    
    gm = GManager(
        groups=grps_dep[IGroups](),
        key=key_dep[IKey](),
        drawer=drw_dep[IDrawer](),
        scene_loader=scene_dep[ISceneLoader](),
        object_setter=obj_setter
        )
    #gm.set_func(set_data)
    gm.scene_loader.scene_load("test2.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()