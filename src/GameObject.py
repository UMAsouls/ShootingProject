import pygame
import os

import Vector as vec

#ピボット（描写位置)
pivots = {
    "topleft":0, "top":1, "topright":2,
    "left":3, "center":4, "right":5,
    "bottomleft":6, "bottom":7, "bottomright":8
    }

#__init__のときの引数の初期値
mem = {
    "path" : "sample.png", "pos": vec.Vector(0,0),
    "name" : "", "tag": ""
}

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def getParentPath(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path

#全てのオブジェクトの基礎
class GameObject(pygame.sprite.DirtySprite):
    #コンストラクタ   
    def __init__(self, **kwargs):
        super().__init__()
        
        for k,v in mem.items():
            if not k in kwargs:
                kwargs[k] = v
        
        path = getParentPath(1)
        self.image = pygame.image.load(path + f"/image/{kwargs['path']}")
        self.rect = self.image.get_rect()
        self.position = kwargs["pos"]
        self.pivot = 0
        self.name = kwargs["name"]
        self.tag = kwargs["tag"]
        self.active = True
    
    #描写位置を変える
    def changePivot(self, piv):
        if(type(piv) is int):
            self.pivot = piv % 9
        elif(piv in pivots):
            self.pivot = pivots[piv]
        else:
            print(f"error: given centence {piv} isn't contained in pivots")
    
    #更新処理  
    def update(self,gm):
        if not self.active:
            return
        
        if(self.pivot == 0):
            self.rect.topleft = self.position.change2list()
        elif(self.pivot == 1):
            self.rect.top = self.position.change2list()
        elif(self.pivot == 2):
            self.rect.topright = self.position.change2list()
        elif(self.pivot == 3):
            self.rect.left = self.position.change2list()
        elif(self.pivot == 4):
            self.rect.center = self.position.change2list()
        elif(self.pivot == 5):
            self.rect.right = self.position.change2list()
        elif(self.pivot == 6):
            self.rect.bottomleft = self.position.change2list()
        elif(self.pivot == 7):
            self.rect.bottom = self.position.change2list()
        elif(self.pivot == 8):
            self.rect.bottomright = self.position.change2list()
        else:
            pass
        
        

    