import os
import tkinter as tk


from PyEasy import PyEasy
from SceneData import SceneData
from GroupsFrame import GroupsFrame

os.chdir(os.path.abspath(os.path.join(__file__,os.pardir)))

PROJECT_PATH = os.path.abspath(os.path.join(os.getcwd(),os.pardir))

test  = SceneData(PROJECT_PATH, "test5.json")
test.load()

master = tk.Tk()

pyeasy = PyEasy(master, test, GroupsFrame(test))
