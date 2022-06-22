a = 10
print(a)
print("data type of :", type(a))

b = 10.5
print(b)
print("data type of :", type(b))

c = 1+3j
print(c)
print("data type of :", type(c))
print("c is complex number", isinstance(1+3j, complex), "\n\n")


# for multiple line string
a = "Amd. Abu Taiab"
print(a)
b = '''
  Md. Abu Taiab
  age 29 years old
  salary = 30000
  '''
print(b)

# add to string
str1 = "Hello Taiab"  #string str1    
str2 = "How Are You"  #string str2    
print(str1[0:2])#printing first two character using slice operator 
print(str1[4]) #printing 4th character of the string 
print(str1*2)#printing the string twice 
print(str1+str2)#printing the concatenation of str1 and str2   
