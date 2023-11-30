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

from ObjectGroup.ObjectGroup import Dependency as grp_dep
from ObjectGroup.SingleGroup import Dependency as sgrp_dep
from Groups.Groups import Dependency as grps_dep
from Key.Key import Dependency as key_dep
from Drawer.Drawer import Dependency as drw_dep
from SceneLoader.SceneLoader import Dependency as scene_dep
from GameObject.GameObject import Dependency as obj_dep


from GameObject.Objectbuillder import Dependencybuillder

def make_obj_from_str(c_name: str):
        if(c_name == ""):
            dep = obj_dep
        else:
            dep = Dependencybuillder(c_name)
            
        obj = dep[IGameObject]()
            
        return obj
    
#jsonデータをセット
#同時にそのjsonでロードされる全てをgroupsに追加  
def set_data(data, groups: IGroups, drawer: IDrawer):
    for d in data["obj"]:
        obj = make_obj_from_str(f"{data['use']}.{d['class']}")
        obj.set_data(d)
        
        if(isinstance(obj, IGameObject)):
            obj: IGameObject
            drawer.add(obj)
            group: ISingleGroup = sgrp_dep[ISingleGroup]()
            group.set_main(obj)
        else:
            group: IObjectGroup = obj
            #json内でグループ型があった際の処理（応急処置：入れ子でも対応すべきか？）
            for d2 in d["data"]:
                obj: IGameObject = make_obj_from_str(f"{data['use']}.{d2['class']}")
                obj.set_data(d2)
                drawer.add(obj)
                group.add(obj)
            
        groups.add_group(group)




def main():
    gm = GManager(grps_dep[IGroups](),key_dep[IKey](),drw_dep[IDrawer](),scene_dep[ISceneLoader]())
    gm.set_func(set_data)
    gm.scene_loader.scene_load("test2.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()