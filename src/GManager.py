import pygame
from pygame.locals import *
import sys
import os

import GameObject as gobj
import Objects as objs
import Vector as vec

from object import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#ゲームの統括クラス
class GManager:
    def __init__(self) -> None:
        pygame.init()
        #ゲーム画面
        self.screen = pygame.display.set_mode([1920,1080], FULLSCREEN)
        #ゲームの全てのオブジェクト
        self.objects = objs.Objects()
        #オブジェクトのグループ
        self.groups = {}
    
    #グループを加える
    def addGroup(self, group) -> None:
        for s in group.sprites():
            s.add(self.objects)
        
        self.groups[group.__class__.__name__] = group
    
    #スプライトを加える  
    def addGameObject(self, obj) -> None:
        obj.add(self.objects)
        
    def start(self) -> None:
        self.obj1 = gobj.GameObject()
        self.obj1.add(self.objects)
        
        for i in os.listdir("object"):
            if i[0] != "_": 
                exec(f"{i}"[0:-3] + ".Start(self)")
        
    def update(self) -> None:
        pygame.display.update()
        self.objects.update(gm)   
        self.objects.draw(self.screen)
                
    def MainLoop(self):
        while True:
            self.update()
        
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
        
        
        
        
if __name__ == "__main__" :
    gm = GManager()
    gm.start()
    gm.MainLoop()