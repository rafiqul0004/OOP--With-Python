x=input()
r=x.split()
final=""
for w in r:
    rev_w=w[::-1]
    final=final+rev_w+' '
print(final[:-1])