import tkinter as tk

from GroupsFrame import GroupsFrame

from SceneData import SceneData

class PyEasy:
    def __init__(
        self,
        window: tk.Tk,
        scene: SceneData,
        groups: GroupsFrame
        ) -> None:
        
        self.window = window
        self.window.title("PyEasy")
        sizex,sizey = self.window.winfo_screenwidth(),self.window.winfo_screenheight()
        
        self.window.geometry(f"{sizex}x{sizey}")
        
        self.scene = scene
        
        self.groups = groups
        
        self.groups.set(
            self.window,
            tk.Frame(self.window, relief=tk.GROOVE, bd= 3),
            scene=self.scene
        )
        
        self.window.bind("<Escape>", lambda e: self.window.destroy())
        
        self.window.mainloop()
        