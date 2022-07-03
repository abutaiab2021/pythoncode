# tup  = ("hi", "Python", 2)    
# # Checking type of tup  
# print (type(tup))    
  
# #Printing the tuple  
# print (tup)  
  
# # Tuple slicing  
# print (tup[1:])    
# print (tup[0:1])    
  
# # Tuple concatenation using + operator  
# print (tup + tup)    
  
# # Tuple repatation using * operator  
# print (tup * 3)     
  
# # Adding value to tup. It will throw an error.  
# t[2] = "hi"  

#ordered list
#()
#inmutable. kono value change,update,delete kora jabe na
#jei khetre value constant thakbe tokhon tuple use korte hobe.
# t=("python","Java")
from itertools import count
from operator import index


t=(10,20,30,40,50,10)
print(type(t))
print()

# l=len(t)
# # print(l)

# for a in range(l):
#     print(t[a])

# another way
for a in t:
    print(a)

m=max(t)
print("maximum value:",m)

n=min(t)
print("minimum value:",n)

c=t.count(10)
print("countable element value:",c)

i=t.index(50)
print("index number for a list value:",i)

s=sum(t)
print("total value of this list:",s)

s2=sum(t,10)
print(s2)
