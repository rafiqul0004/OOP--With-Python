r=input()
s=[]
c=""
for char in r:
    c=c+char
    if c.count("L")==c.count("R"):
        s.append(c)
        c=""
print(len(s))
for st in s:
    print(st)
