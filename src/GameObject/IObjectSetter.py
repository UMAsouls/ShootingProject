import abc

class IObjectSetter(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def add_obj(data) -> None:
        pass