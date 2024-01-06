from typing import Any

import json

#シーンのデータをまとめて管理してる
class SceneData:
    
    def __init__(self, path: str, name: str) -> None:
        self.path = path
        self.name = name
        self.objects: list[dict[str, Any]] = []
        self.groups: list[dict[str, Any]] = []
    
    def load(self):
        with open(self.path + "/json/" + self.name) as f:
            data = json.load(f)
            
        if(data["type"] == "scene"):
            self.objects = data["obj"]
            self.groups = data["grp"]
    
    def save(self):
        data: dict[str, Any] = {"type": "scene", "obj": [], "grp": []}
        data["obj"] = self.objects
        data["grp"] = self.groups
        
        with open(self.path + "/json/" + self.name, "w") as f:
            json.dump(data, f, indent=2)