import injector

from . import IDrawer
from . import IGroups

from GManager import IObjectSetter as I0

class ObjectSetter(I0):
    
    @injector.inject
    def __init__(self, groups: IGroups, drawer: IDrawer):
        self.add_obj_tmp: function = None
        self.add_group_tmp: function = None
        self.groups: IGroups = groups
        self.drawer: IDrawer = drawer
    
    def set_func(self, add_obj, add_group) -> None:
        self.add_obj_tmp = add_obj
        self.add_group_tmp = add_group
        
    def add_obj(self, data: dict) -> None:
        self.add_obj_tmp(data, self.groups, self.drawer)
    
    def add_group(self, data: dict) -> None:
        self.add_group_tmp(data, self.groups, self.drawer)
        
    def set_data(self, data: dict) -> None:
        for d in data["obj"]:
            self.add_obj(d)
        
        for d in data["grp"]:
            self.add_group(d)


from DependencyMaker import DependencyMaker
from Drawer import Drawer
from Groups import Groups

class Dependencybuillder(DependencyMaker):
    
    @classmethod
    def configure(cls, binder: injector.Binder):
        binder.bind(I0, to=ObjectSetter)
        
        binder.bind(IDrawer, to=Drawer)
        binder.bind(IGroups, to=Groups)
        
        
Dependency = Dependencybuillder()