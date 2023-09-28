balance=5000
def buy_things(iteam,price):
    global balance
    print('total balance : ',balance)
    balance=balance-price
    print(f'Balance after buying {iteam}: {balance}')
buy_things('Apple',300)
def add_money(amount):
    global balance
    print("Total Balance : ",balance)
    balance=balance+amount
    print('Total balance after adding : ',balance)
add_money(5000)
