class Product:
    def __init__(self,name,price,stock) -> None:
        self.name=name
        self.price=price
        self.stock=stock
class Shop:
    def __init__(self) -> None:
        self.products=[]
    def add_product(self,name,price,stock):
        new_product=Product(name,price,stock)
        self.products.append(new_product)
    def buy_product(self,p_name,quantity):
        for product in self.products:
            if product.name==p_name:
                if product.stock>0 and product.stock>=quantity:
                    product.stock-=quantity
                    return f'Congratulations'
                else :
                    return f'{p_name} is not available in stock'
        return f'{p_name} is not in shop'
r=Shop()
r.add_product("Apple",300,5)
r.add_product("Orange",200,7)
r.add_product("Lemon",100,10)
print(r.buy_product("Orange",3))
print(r.buy_product("Orange",25))
print(r.buy_product("Water_Mellon",3))
print(r.buy_product("Apple",5))
print(r.buy_product("Apple",1))