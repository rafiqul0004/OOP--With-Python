class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_balance=100
        self.max_balance=100000
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'After deposit your balance is : {self.get_balance()}')
    def withdraw(self,amount):
        if amount>self.max_balance:
            print(f'Sorry You cannot withdraw max : {self.max_balance} ')
        elif amount<self.min_balance:
            print(f'Sorry you cannot withdraw below : {self.min_balance}')
        else:
            self.balance-=amount
            print(f'Here is Your Amount : {amount}')
            print(f'After withdraw your amount if {self.get_balance()}')
DBBL=Bank(20000)
DBBL.deposit(1000)
DBBL.withdraw(10)
DBBL.withdraw(5000)