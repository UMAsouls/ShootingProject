import json
import os
from typing import List
import injector

from GManager import ISceneLoader as I0
from GameObject import ISceneLoader as I1

from DependencyMaker import DependencyMaker

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path

PROJECT_PATH = os.path.dirname(os.getcwd())

class SceneLoader(I0,I1,Singleton):
    def __init__(self) -> None:
        if hasattr(self, "_isinited"):
            return
        
        self.isinited = True
        
        self._scene_data: List[str] = []
        self._end_scene : bool = False
        
    def scene_load(self, path: str) -> None:
        path = PROJECT_PATH + "/json/" + path
        with open(path) as f:
            data = json.load(f)
            
        self._scene_data = data
        self._end_scene = True
        
    
    @property
    def scene_data(self):
        data = self._scene_data
        self._scene_data = []
        return data
    
    @property
    def end_scene(self) -> bool:
        tmp = self._end_scene
        self._end_scene = False
        return tmp
    

class Dependencybuillder(DependencyMaker):
    
    @classmethod
    def configure(cls, binder: injector.Binder):
        binder.bind(I0, to=SceneLoader)
        binder.bind(I1, to=SceneLoader)
        
Dependency = Dependencybuillder()