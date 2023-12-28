import os
import pygame
from pygame.locals import *
from typing import Any

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

from ObjectSetter.set_functions import add_obj,add_group,make_obj_from_data

def main():
    obj_setter: IObjectSetter = Dependency[IObjectSetter]()
    obj_setter.set_func(add_obj, add_group, make_obj_from_data)
    obj_setter.set_dependency(Dependency[IGroups]() ,Dependency[IDrawer]())
    
    gm = GManager(
        groups=Dependency[IGroups](),
        key=Dependency[IKey](),
        drawer=Dependency[IDrawer](),
        scene_loader=Dependency[ISceneLoader](),
        object_setter=Dependency[IObjectSetter]()
        )
    #gm.set_func(set_data)
    gm.scene_loader.scene_load("testtitle.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()