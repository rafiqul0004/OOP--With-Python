import math
import time
def timmer(func):
    def inner(*args,**kwargs):
        print("Time started")
        start=time.time()
        func(*args,**kwargs)
        print("Time Ended")
        end=time.time()
        print(f'Total time taken : {end-start}')
    return inner
@timmer
def get_factorial(n):
    print("Factorial Started")
    result=math.factorial(n)
    print(f'factorial of {n} : {result}')
get_factorial(n=6)
