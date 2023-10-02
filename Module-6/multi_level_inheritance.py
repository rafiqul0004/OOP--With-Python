class Vehicle:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __repr__(self) -> str:
        return f'{self.brand}   {self.price}'
class Bus(Vehicle):
    def __init__(self, brand, price,seat):
        self.seat=seat
        super().__init__(brand, price)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
class Truck(Vehicle):
    def __init__(self, brand, price,weight):
        self.weight=weight
        super().__init__(brand, price)
class PickUp(Truck):
    def __init__(self, brand, price, weight):
        super().__init__(brand, price, weight)
class AcBus(Bus):
    def __init__(self, brand, price, seat,temparature):
        self.temperature=temparature
        super().__init__(brand, price, seat)
    def __repr__(self) -> str:
        print( f'{self.temperature}')
        return super().__repr__()
acBus=AcBus('Scania',1000000,22,18)
print(acBus)