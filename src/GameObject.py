import pygame
import Vector

pivots = {
    "topleft":0, "top":1, "topright":2,
    "left":3, "center":4, "right":5,
    "bottomleft":6, "bottom":7, "bottomright":8
    }

class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface()
        self.rect = self.image.get_rect()
        self.position = Vector(0,0)
        self.pivot = 0
        
    def __init__(self, **kwargs):
        self.image = pygame.Surface(kwargs["path"])
        self.rect = self.image.get_rect()
        self.position = Vector(kwargs["x"], kwargs["y"])
        self.pivot = 0
        
    def changePivot(self, piv):
        if(type(piv) is int):
            self.pivot = piv % 9
        elif(piv in pivots):
            self.pivot = pivots[piv]
        else:
            print(f"error: given centence {piv} isn't contained in pivots")
            
    def update(self):
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
    