class phone:
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price
my_phone=phone('Me','Samsung',29000)
print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone=phone('I don\'t know her','Iphone',400000)
print(her_phone.owner,her_phone.brand,her_phone.price)