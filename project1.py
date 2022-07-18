import random
Cnumber=random.randrange(1,101)
UserInput=int(input("Enter the value:--"))
if Cnumber>UserInput :
    print("Computer Number:",Cnumber)
    print("Your Gess Number too low")
elif UserInput>Cnumber:
    print("Computer Number:",Cnumber)
    print("Your Gess number is too high")
else:
    print("Computer Number:",Cnumber)
    print("Your Gess number is equal to computer number.")