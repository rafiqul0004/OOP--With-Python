class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
    ## getter is readonly method
    @property
    def age(self):
        return self._age
    @property
    def salary(self):
        return self.__money
    ##setter is read only and write
    @salary.setter
    def salary(self,value):
        if value<0:
            return 'Salary cannot be negative'
        self.__money+=value
r=User('Rahat',23,20000)
print(r.age)
print(r.salary)
r.salary=2000
print(r.salary)