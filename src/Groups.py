import pygame
import injector

from IGroups import IGroups
from IObjectGroup import IObjectGroup
from IGameObject import IGameObject
from ISingleGroup import ISingleGroup

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Groups(IGroups, Singleton):
    def __init__(self) -> None:
        if hasattr(self, "_isinit"):
            return
            
        self._groups = {}
        self._singles = {}
        self._types = {}
        self._isinit = True
                        
    def init(self) -> None:
        del self._isinit
        self.__init__()
        
    def get_group_by_name(self, name:str) -> IObjectGroup:
        return self._groups[name]
    
    def add_group(self, group: IObjectGroup) -> IObjectGroup:
        if group.name in self._groups:
            print(self._groups, group.name)
            print("\nERROR: Don't put same name object or group\n")
            raise ArithmeticError()
        
        self._groups[group.name] = group
        if isinstance(group, ISingleGroup):
            self._singles[group.name] = group
        
        
    def get_single_by_name(self, name:str) -> IGameObject:
        single: ISingleGroup = self._singles[name]
        return single.get_main()
    
    def get_group_by_type(self) -> IObjectGroup:
        return
    
    
    
class Dependencybuillder:
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        #
        binder.bind(IGroups, to=Groups)
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    

Dependency = Dependencybuillder()