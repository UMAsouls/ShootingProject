import pygame
import Vector as vec
import os

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

#全てのオブジェクトの基礎
class GameObject(pygame.sprite.Sprite):
    #コンストラクタ   
    def __init__(self, **kwargs):
        super().__init__()
        
        for k,v in mem.items():
            if not k in kwargs:
                kwargs[k] = v
        
        os.chdir("..")
        self.image = pygame.image.load("image/" + kwargs["path"])
        os.chdir("src")
        self.rect = self.image.get_rect()
        self.position = kwargs["pos"]
        self.pivot = 0
        self.name = kwargs["name"]
        self.tag = kwargs["tag"]
        self.active = True
    
    
    def changePivot(self, piv):
        if(type(piv) is int):
            self.pivot = piv % 9
        elif(piv in pivots):
            self.pivot = pivots[piv]
        else:
            print(f"error: given centence {piv} isn't contained in pivots")
            
    def update(self):
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
        
        

    