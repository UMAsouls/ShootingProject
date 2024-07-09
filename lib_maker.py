import os

PATH = "object"

def make_import(path,mod):
    prog = ""
    
    for k in filter(lambda x: x[0] != "_" and x[0] != ".",
        os.listdir(path)):
        p = os.path.abspath(f"{path}\\{k}")
        print(p)
        if(os.path.isfile(p) and k[-3:] == ".py"):
            prog += f"from {mod} import {k[0:-3]}\n"
        
        elif(os.path.isdir(p)): 
            make_import(f"{path}\\{k}", f"{mod}.{k}")
            prog += f"from {mod} import {k}\n"
            
    with open(f"{path}//__init__.py","w",encoding="utf-8") as f:
        f.write(prog)
        
        
if __name__ == "__main__":
    make_import(PATH,PATH)
        
        