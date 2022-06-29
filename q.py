l=[]
while True:
    c=int(input('''
    1 push element
    2 pop element
    3 font element
    4 last element
    5 display
    6 exit
    '''))
    if c==1:
        n=input("Enter the value : ");
        l.append(n)
        print(l)
    elif c==2:
        if len(l) ==0:
            print("Empty Queue")
        else:
            del l[0]
            
            print(l)
    elif c==3:
         if len(l) ==0:
            print("Empty Queue")
         else:
            print("First Element Vlaue",l[0])   
    elif c==4:
         if len(l) ==0:
            print("Empty Queue")
         else:
            print("Last Element Vlaue",l[-1])   
    elif c==5:
        print("Display Queue",l)
    elif c==6:
        break
    else:
        print("Invid Operation")