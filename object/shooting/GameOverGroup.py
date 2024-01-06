import pygame

from pygameEasy.ObjectGroup import ObjectGroup

from .Base import Base
from .Counter import Counter
from .GameOverText import GameOverText

class GameOverGroup(ObjectGroup):
    def set_data(self, data: dict) -> None:
        super().set_data(data)
        
        self.base: Base = self.get_obj_by_id("base")
        self.counter: Counter = self.get_obj_by_id("counter")
        self.text: GameOverText = self.get_obj_by_id("text")
        self.select1: GameOverText = self.get_obj_by_id("select1")
        self.select2: GameOverText = self.get_obj_by_id("select2")
        
        self.winner = ""
        self.over: bool = False
    
    #選択肢を選択するプログラム
    def selecter(self):
        pass
    
    def text_set(self):
        self.text.visible = True
        self.select1.visible = True
        self.select2.visible = True
        
        self.text.change_pivot("center")
        self.select1.change_pivot("center")
        self.select2.change_pivot("center")
        
        size = pygame.display.get_surface().get_size()
        
        self.text.position = [size[0]//2, size[1]*4//10]
        self.select1.position = [size[0]//2, size[1]*6//10]
        self.select2.position = [size[0]//2, size[1]*7//10]
        
        self.text.text += self.winner
        
    def update(self):
        super().update()
        
        if self.over:
            self.selecter()
            return
        
        if self.base.get_hp_ratio() <= 0:
            self.winner = "Attack"
            self.over = True
            self.text_set()
            
        elif self.counter.count <= 0:
            self.winner = "Defense"
            self.over = True
            self.text_set()
        
        