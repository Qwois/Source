import asyncio

class MainThread:
    def  __init__(self):
        pass

    def start_generation(self):
        print(f"Start!\n")

if "__main__" == __name__:
    main = MainThread()
    main.start_generation()