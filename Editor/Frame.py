import tkinter as tk
import abc

from SceneData import SceneData

class Frame(tk.Frame, metaclass = abc.ABCMeta):
    
    def __init__(self) -> None:
        pass
        
    def set(self, frame: tk.Frame, scene: SceneData) -> None:
        self._frame = frame
        self._scene = scene