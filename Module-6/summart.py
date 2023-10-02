class Book:
    def __init__(self,name) -> None:
        self.name=name
    def read(self):
        raise NotImplementedError
class Physics(Book):
    def __init__(self, name,lab) -> None:
        self.lab=lab
        super().__init__(name)
    def read(self):
        print("Reading Physics")
topon_sir=Physics('Topon_sir',True)
print(issubclass(Physics,Book))
print(isinstance(topon_sir,Physics))
topon_sir.read()