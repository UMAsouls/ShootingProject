from GManager import GManager


def main():
    gm = GManager()
    gm.scene_loader.scene_load("test2.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()