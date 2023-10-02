class Gadget:
    def __init__(self,brand,price,colour,origin):
        self.brand=brand
        self.price=price
        self.colour=colour
        self.origin=origin
    def run(self):
        return f'Running The device : {self.brand}'
class Laptop(Gadget):
    def __init__(self, brand, price, colour, origin,ssd):
        self.ssd=ssd
        super().__init__(brand, price, colour, origin)
    def coding(self):
        return f'Coding and Practicing'
    def __repr__(self) -> str:
        return f'{self.brand} {self.price} {self.colour} {self.ssd}'
        return super().__repr__()
    
class Phone:
    def __init__(self,dual_sim):
        self.dual_sim=dual_sim
    def call(self,number,text):
        return f'Calling to the number : {number} and sendind : {text}'
class Camera:
    def __init__(self,pixel):
        self.pixel=pixel
    def change_lens(self):
        pass
my_laptop=Laptop('Asus',65000,'Silver','China',128)
print(my_laptop)