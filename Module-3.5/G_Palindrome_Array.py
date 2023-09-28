n=int(input())
l=list(map(int,input().split()))
r=l[::-1]
if r==l:
    print("YES")
else:
    print("NO")