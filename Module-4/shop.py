class shop:
    cart=[] #class attribute
    def __init__(self,buyer):
        self.buyer=buyer
    def add_to_cart(self,iteam):
        self.cart.append(iteam)
r=shop('Rahat')
r.add_to_cart('Phone')
print(r.cart)
p=shop('PPPPP')
p.add_to_cart('Watch')
print(p.cart)