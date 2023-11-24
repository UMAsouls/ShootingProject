import json
import os
from typing import List
import injector

from ISceneLoader import ISceneLoader

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

class SceneLoader(ISceneLoader,Singleton):
    def __init__(self) -> None:
        if hasattr(self, "_isinited"):
            return
        
        self.isinited = True
        
        self._scene_data: List[str] = []
        self._end_scene : bool = False
        
    def scene_load(self, path: str) -> None:
        path = get_parent_path(1) + "/json/" + path
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
        binder.bind(ISceneLoader, to=SceneLoader)
        
Dependency = Dependencybuillder()