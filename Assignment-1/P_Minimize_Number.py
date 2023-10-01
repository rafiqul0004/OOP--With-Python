n = int(input())
l = list(map(int, input().split()))
op = 0
def func(ls):
    for i in ls:
        if i % 2 != 0:
            return 0
    return 1
while func(l):
    l = [i // 2 for i in l]
    op += 1
print(op)


