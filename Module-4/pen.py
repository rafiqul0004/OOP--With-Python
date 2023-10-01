class pen:
    def __init__(self,brand,ink_colour,price):
        self.brand=brand
        self.ink_colour=ink_colour
        self.price=price
m=pen('High School','Red',10)
print(m.brand,m.ink_colour,m.price)
n=pen('All Time','Blue',15)
print(n.brand,n.ink_colour,n.price)
p=pen('Topper','Black',5)
print(p.brand,p.ink_colour,p.price)