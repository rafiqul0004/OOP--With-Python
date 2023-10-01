class shop:
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]
    def add_to_cart(self,iteam):
        self.cart.append(iteam)
r=shop('Rahat')
r.add_to_cart('Phone')
r.add_to_cart('Glass')
print(f"{r.buyer} : {r.cart}")
p=shop('PPPPP')
p.add_to_cart('Watch')
print(f"{p.buyer} : {p.cart}")
