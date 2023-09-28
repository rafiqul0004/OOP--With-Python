# def person(first,last):
#     name= f"{first} {last}"
#     return name
# name=person('Rafiqul','Islam')
# print(name)


# Using key
# def person(first,last):
#     name= f"{first} {last}"
#     return name
# name=person(last='Islam', first='Rafiqul')
# print(name)

# Using kargs
def person(first,last,**addition):
    name= f"{first} {last}"
    for key,value in addition.items():
        print(key,value)
    return name
name=person(first='Rafiqul',last='Islam',nickname='Rahat')
print(name)

# Multiple return
def cal(num1,num2):
    sum=num1+num2
    sub=num1-num2
    multi=num1*num2
    div=num1/num2
    return sum,sub,multi,div
a=input()
b=input()
cal=cal(int(a),int(b))
print(cal)