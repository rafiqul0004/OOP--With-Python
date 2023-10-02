class Animal:
    def __init__(self,name) -> None:
        self.name=name
    def make_sound(self):
        print("Making sound")
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Meaow Meaow")
class Bird(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Kichir Michir")
class Cow(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Hamba Hamba")
mini =Cat('Mini')
popo=Bird('Popo')
sundari=Cow('Sundari')
animals=[mini,popo,sundari]
for animal in animals:
    print(animal.name)
    animal.make_sound()