import json
import os
import injector

from GManager import ISceneLoader as I0
from GameObject import ISceneLoader as I1
from ObjectSetter import ISceneLoader as I2

from Singleton import Singleton

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path

PROJECT_PATH = os.path.dirname(os.getcwd())

@injector.singleton
class SceneLoader(I0,I1,I2, Singleton):
    _scene_data: list[str] = []
    _end_scene: bool = False
        
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
    

from DependencyConfig import Config

configs = [
    Config(I0, lambda: SceneLoader.get_instance()),
    Config(I1, lambda: SceneLoader.get_instance()),
    Config(I2, lambda: SceneLoader.get_instance())
]