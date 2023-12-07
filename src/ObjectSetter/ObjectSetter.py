import injector

from . import IDrawer
from . import IGroups

from GManager import IObjectSetter as I0
from GameObject import IObjectSetter as I1

@injector.singleton
class ObjectSetter(I0, I1):
    
    def __init__(self):
        self.add_obj_tmp = None
        self.add_group_tmp = None
        self._groups: IGroups = None
        self._drawer: IDrawer = None
        
    def set_func(self, add_obj, add_group) -> None:
        self.add_obj_tmp = add_obj
        self.add_group_tmp = add_group
        
    def set_dependency(self, groups: IGroups, drawer: IDrawer):
        self._groups: IGroups = groups
        self._drawer: IDrawer = drawer
        
    def add_obj(self, data: dict) -> None:
        self.add_obj_tmp(data, self._groups, self._drawer)
    
    def add_group(self, data: dict) -> None:
        self.add_group_tmp(data, self._groups, self._drawer)
        
    def set_data(self, data: dict) -> None:
        for d in data["obj"]:
            self.add_obj(d)
        
        for d in data["grp"]:
            self.add_group(d)


from DependencyConfig import Config

configs = [
    Config(I0, ObjectSetter),
    Config(I1, ObjectSetter)
]