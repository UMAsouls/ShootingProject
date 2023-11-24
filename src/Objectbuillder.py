import injector
import os

from IGameObject import IGameObject
from IObjectGroup import IObjectGroup
from IGroups import IGroups
from Groups import Groups
from IKey import IKey
from Key import Key
from IDrawer import IDrawer
from Drawer import Drawer
from ISceneLoader import ISceneLoader
from SceneLoader import SceneLoader

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#objectから全てimport
for i in os.listdir("object"):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if i[0] == "_" or i[0] == ".": 
        continue
    exec(f"from object" + " import " + f"{i}")

class Dependencybuillder:
    def __init__(self, name: str, isgroup: bool = False):
        self.name: str = name
        self.isgroup: bool = isgroup
        self._injector = injector.Injector(self.configure)
    
    #injectorの初期化処理
    def configure(self, binder: injector.Binder):
        path = self.name.split(".")
        if(self.isgroup):
            binder.bind(IObjectGroup, to=eval(f"{path[0]}.{path[1]}.{path[1]}"))
        else:
            #IGameObjectにGameObjectを紐づけ
            binder.bind(IGameObject, to=eval(f"{path[0]}.{path[1]}.{path[1]}")) 
        #
        binder.bind(IGroups, to=Groups)
        #
        binder.bind(IKey, to=Key)
        #
        binder.bind(IDrawer, to=Drawer)
        #
        binder.bind(ISceneLoader, to=SceneLoader)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    