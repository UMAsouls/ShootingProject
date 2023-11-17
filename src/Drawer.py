import pygame

from IGameObject import IGameObject

class Drawer:
    objects:pygame.sprite.LayeredDirty = pygame.sprite.LayeredDirty()
    
    @classmethod
    def add(cls, obj: IGameObject):
        cls.objects.add(obj)
        
    @classmethod
    def draw(cls, screen: pygame.Surface):
        cls.objects.draw(screen)
        
    @classmethod
    def update(cls):
        rect_list = []
        for i in cls.objects.sprites():
            if i.moving: rect_list.append(i.rect)
            
        cls.objects.update()
        
        for i in cls.objects.sprites():
            if i.moving: rect_list.append(i.rect)
            
        print(len(rect_list))
            
        pygame.display.update(rect_list)
            
        