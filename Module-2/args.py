def sum(*args):
    sum=0
    print(args)
    for num in args:
        sum+=num
    return sum
total=sum(3,2,4,5)
print(total)
