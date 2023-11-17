from GManager import GManager


def main():
    gm = GManager()
    gm.scene_load("test.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()