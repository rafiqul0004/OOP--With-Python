class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def multi(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2
calculator=Calculator()
print(calculator.add(30,5))
print(calculator.sub(30,5))
print(calculator.multi(30,5))
print(calculator.div(30,5))