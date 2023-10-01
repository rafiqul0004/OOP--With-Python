n=int(input())
r=list(map(int,input().split()))
c={}
for i in r:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
final=0
for k,v in c.items():
    if v!=k:
        if k<v:
            final=final+(v-k)
        else:
            final=final+v
print(final)

