from pygameEasy.ObjectGroup import ObjectGroup

from .Base import Base
from .Counter import Counter
from .GameOverText import GameOverText

class GameOverGroup(ObjectGroup):
    def set_data(self, data: dict) -> None:
        super().set_data(data)
        
        base: Base = self.get_obj_by_id("base")
        counter: Counter = self.get_obj_by_id("counter")
        text: GameOverText = self.get_obj_by_id("text")
        select1: GameOverText = self.get_obj_by_id("select1")
        select2: GameOverText = self.get_obj_by_id("select2")
        
    def update(self):
        super().update()