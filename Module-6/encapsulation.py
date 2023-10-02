class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name #Public
        self._branch='Agrabad' #Protected
        self.__balance=initial_deposit #Private
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
rahat=Bank('Rafiqul',20000)
print(rahat._branch)
rahat.deposit(5000)
print(rahat.holder_name)
print(rahat.getBalance())
rahat.withdraw(2000)
print(rahat.getBalance())
#Accessing Private attrubute:
#print(dir(rahat))
#print(rahat._Bank__balance)