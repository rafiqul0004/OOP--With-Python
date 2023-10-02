from abc import ABC,abstractmethod
class Pet(ABC):
    @abstractmethod
    def eat(self):
        print("I am eatting")
    @abstractmethod
    def move(self):
        print("I am Moving")
class Cat(Pet):
    def __init__(self,name) -> None:
        self.name=name
        super().__init__()
    def eat(self):
        print("I am eating fish")
    def move(self):
        print("Now, I am Moving")
mini=Cat('Mini')
mini.eat()
mini.move()