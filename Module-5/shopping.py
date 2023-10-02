class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,iteam,price,quantity):
        product={'iteam':iteam, 'price':price,'quantity':quantity}
        self.cart.append(product)
    def checkout(self,amount):
        total=0
        for iteam in self.cart:
            total+=iteam['price']*iteam['quantity']
        if amount<total:
            print(f'Please pay {total-amount} more')
        else:
            extra=amount-total
            print(f'Here is your products and extra : {extra}')
    def remove_from_cart(self,iteam_name):
        for iteams in self.cart:
            if iteams['iteam']==iteam_name:
                index=self.cart.index(iteams)
                self.cart.pop(index)
        print(self.cart)
r=Shopping('Rahat')
r.add_to_cart('chips',10,3)
r.add_to_cart('Chollate',20,2)
r.add_to_cart('juice',30,3)
r.remove_from_cart('juice')
r.checkout(500)