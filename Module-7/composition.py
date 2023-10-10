## inheritance 'is a' relation
##composition 'has a' relation
class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        print("Engine Started")
class Driver:
    def __init__(self) -> None:
        pass
class car:
    def __init__(self) -> None:
        self.engine=Engine()
        self.driver=Driver()
    def start(self):
        self.engine.start()