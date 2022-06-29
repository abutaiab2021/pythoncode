l=[]
while True:
    c=int(input('''
    1 push element
    2 pop element
    3 peek element
    4 display
    5 exit
    '''))
    if c==1:
        n=input("Enter the value : ");
        l.append(n)
        print(l)
    elif c==2:
        if len(l) ==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
         if len(l) ==0:
            print("Empty Stack")
         else:
            print("Last Element Vlaue",l[-1])   
    elif c==4:
        print("Display Stack",l)
    elif c==5:
        break
    else:
        print("Invid Operation")