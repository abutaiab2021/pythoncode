l=[10,20,30,40]
l1=[50,60,70,80]

t=len(l)

# one way
for a,b in zip(l,l1):
    print(a,b,"\n")

# another way
for h in range(t):
    print(l[h],l1[h])