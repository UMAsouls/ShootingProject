import injector

from IGameObject import IGameObject
from GameObject import GameObject
from IObjectGroup import IObjectGroup
from ObjectGroup import ObjectGroup
from IGroups import IGroups
from Groups import Groups

class Dependencybuillder:
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #IGameObjectにGameObjectを紐づけ
        binder.bind(IGameObject, to=GameObject)
        #
        binder.bind(IObjectGroup, to=ObjectGroup)
        #
        binder.bind(IGroups, to=Groups, scope=injector.SingletonScope)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    

Dependency = Dependencybuillder()
