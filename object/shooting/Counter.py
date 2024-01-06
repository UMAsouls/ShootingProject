from pygameEasy.GameObject import TextObject

class Counter(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
        self.count = data["count"]
        
    def update(self) -> None:
        self.text = f"{self.count}"
        
        self.count -= 1