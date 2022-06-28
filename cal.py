print(
    '''
    + add
    - sub
    * multiply
    / devide
    '''
)

num1 =int(input("Enter the value no-1:"))
num2 =int(input("Enter the value no-2:"))
opr=input("Enter the operator...(+,-,*,/) : ")

if (opr == "+"):
    print("additon result: ",num1+num2)
elif (opr == "-"):
    print("sub result: ",num1-num2)
elif (opr == "*"):
    print("multiply result: ",num1*num2)
elif (opr == "/"):
    print("division result: ",num1/num2)
else:
    print("Invalid Operator")
