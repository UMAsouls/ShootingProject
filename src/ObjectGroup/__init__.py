from ObjectGroup.IGameObject import *
#ObjectGroupが先にimportされるとエラー発生
#IGameObjcetが先にimportされないと色々とめんどくさいことになる
#ObjectGroup内の from . import IGameObject でIGameObjectを持ってきてるから先にしないとObjectGroup内でIGameObjectがただのモジュールになる
from ObjectGroup.ObjectGroup import *
#from ObjectGroup.SingleGroup import *