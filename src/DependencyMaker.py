import injector
import abc

#DIコンテナ     
class DependencyMaker(metaclass=abc.ABCMeta):
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    @abc.abstractclassmethod
    def configure(cls, binder: injector.Binder):
        raise NotImplementedError()
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    
