#simple function
def sim_func():
    print("Praramount Isurance Company Limited.")
sim_func()
sim_func()
sim_func()
sim_func()


#function create with arguments
def sum_data(a,b):
    print(a+b)
n1=int(input("Enter the value one:-"))
n2=int(input("Enter the value two:-"))
sum_data(n1,n2)

#function create with arguments
def sum_data2(a,b=5):
    print(a+b)
# n1=int(input("Enter the value one:-"))
# n2=int(input("Enter the value two:-"))
sum_data2(20,20)


#function create with arguments with return keyword
def sum_data2(a,b=5):
    c=(a+b)
    return c
output=sum_data2(20,30)
print("Last Function:",output)