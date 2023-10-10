class Shopping:
    cart=[] #global attribute
    def __init__(self,name) -> None:
        self.name=name
    @classmethod
    def purchase(self,iteam):
        print(self.name)
        print("Nothing to but jus",iteam)
    @staticmethod
    def multiply(a,b):
        print(a*b)
r=Shopping('Bashundara')
r.purchase('Lungi')
Shopping.purchase('Shirt')
Shopping.multiply(2,3)