import pygame
from pygame.locals import *
import sys

import GameObject as gobj
import Objects as objs
import Vector as vec

class GManager:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([1200,800])
        
        self.objects = objs.Objects()
        self.obj1 = gobj.GameObject()
        self.obj1.add(self.objects)
        
    def mainloop(self):
        while True:
            pygame.display.update()
            
            self.objects.update()
            self.objects.draw(self.screen)
        
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
        
        
        
        
if __name__ == "__main__" :
    gm = GManager()
    gm.mainloop()