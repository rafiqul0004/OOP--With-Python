def double_decker():
    print('Its inner double decker')
    def inner_func():
        print("Ints inner func")
    return inner_func
double_decker()()
def working(work):
    print("I am Busy")
    work()
    print("Work Ended")
def coding():
    print("I am coding python")
working(coding)