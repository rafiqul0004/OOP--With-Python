class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print("eating fast food")
    def exercise(self):
        raise NotImplementedError
class Crickter(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team=team
        super().__init__(name, age, height, weight)
    def eat(self):
        print("Vegitables")
    def exercise(self):
        print("Always")
    ##+ overload
    def __add__(self,other):
        return self.name+other.name
    ## * Overload
    def __mul__(self,other):
        return self.age*other.age
    ## > overload
    def __gt__(self,other):
        return self.age>other.age
r=Crickter('Rahat',23,65,000,'My')
p=Crickter('Donot know',22,59,00,'Who Knows')
r.eat()
p.exercise()
print(r+p)
print(r*p)
print(r>p)