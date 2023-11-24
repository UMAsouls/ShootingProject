import pygame
from pygame.locals import *
import os

#pythonでは実行ディレクトリがroot
#src内のものをimportするためカレントディレクトリ移動
os.chdir("../..")


from GameObject import GameObject
from Vector import Vector

class TestGoal(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
    def update(self):
        super().update()
        test_obj = self._groups.get_single_by_name("test")
        
        if(pygame.sprite.collide_rect(self,test_obj)):
            self._scene_loader.scene_load("")
        
        
        
        
    