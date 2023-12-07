import abc

class IObjectSetter(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def set_func(self, add_obj, add_group) -> None:
        pass
    
    @abc.abstractclassmethod
    def set_data(data: dict):
        pass