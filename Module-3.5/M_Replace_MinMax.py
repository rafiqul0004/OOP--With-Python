n=int(input())
l=list(map(int,input().split()))
min_v=min(l)
max_v=max(l)
min_in=l.index(min_v)
max_in=l.index(max_v)
l[min_in]=max_v
l[max_in]=min_v
print(*l)