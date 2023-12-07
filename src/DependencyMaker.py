import injector

from dataclasses import dataclass

from DependencyConfig import Config

#DIコンテナ     
class DependencyMaker:
    __config_list: list[Config] = []
    
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        for i in cls.__config_list:
            binder.bind(i.interface,to=i.cls,scope=i.scope)
            
    @classmethod
    def set(cls, configs: list[Config]) -> None:
        
        for c in configs:
            cls.__config_list.append(c)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    
from Groups.Groups import configs as c1
DependencyMaker.set(c1)
from Drawer.Drawer import configs as c2
DependencyMaker.set(c2)
from SceneLoader.SceneLoader import configs as c3
DependencyMaker.set(c3)
from ObjectSetter.ObjectSetter import configs as c4
DependencyMaker.set(c4)
from Key.Key import configs as c5
DependencyMaker.set(c5)
from ObjectGroup.SingleGroup import configs as c6
DependencyMaker.set(c6)

Dependency = DependencyMaker()