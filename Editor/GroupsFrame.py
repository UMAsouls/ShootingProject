import tkinter as tk

from SceneData import SceneData

from Frame import Frame


class GroupsFrame(Frame):
    
    def __init__(self, scene: SceneData) -> None:
        
        pass
    
    def set(self, master: tk.Tk(), frame: tk.Frame, scene: SceneData) -> None:
        super().set(frame, scene)
        self.window = master
        self._obj_frame = tk.Frame(self._frame, relief=tk.RIDGE, bd = 3)
        self._grp_frame = tk.Frame(self._frame, relief=tk.RIDGE, bd = 3)
        
        self._obj_lavel = tk.Label(self._obj_frame, relief=tk.RAISED, bd= 2, text= "Objects")
        self._grp_lavel = tk.Label(self._grp_frame, relief=tk.RAISED, bd= 2, text= "Groups")
        
        self._obj_lavel.pack(anchor=tk.CENTER)
        self._grp_lavel.pack(anchor=tk.CENTER)
        
        self.make_obj_lavels()
        self.make_grp_lavels()
        
        self._obj_frame.pack()
        self._grp_frame.pack()
        
        self._frame.pack()
        
    def make_obj_lavels(self):
        for i in self._scene.objects:
            lavel = tk.Label(self._obj_frame, relief=tk.SOLID, bd = 1, text=i["name"])
            lavel.pack(anchor=tk.W,fill=tk.X)
            
    def make_grp_lavels(self):
        for i in self._scene.groups:
            lavel = tk.Label(self._grp_frame, relief=tk.SOLID, bd = 1, text=i["name"])
            lavel.pack(anchor=tk.W,fill=tk.X)
        
    