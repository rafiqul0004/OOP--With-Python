n,q=map(int,input().split())
l=list(map(int,input().split()))
for _ in range(q):
    q1,q2=map(int,input().split())
    s=sum(l[q1-1:q2])
    print(s)