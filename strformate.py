w="Welcome to {fname} {lname}".format(fname="Md Abu",lname="Taiab")
print(w)

#for index wise
w1="Welcome to {1} {0}".format("Paramont","Insurance")
print(w1)

#empty braket
w2="Welcome to {} {}".format("Kasem","Mia")
print(w2)

w="Welcome  {a:10} to {b} Paramount".format(a=10,b=30)
print(w)
w="Welcome  {a:^10} to {b} Paramount".format(a=10,b=30)#
print(w)
w="Welcome  {a:<10} to {b} Paramount".format(a=10,b=30)
print(w)
w="Welcome  {a:>10} to {b} Paramount".format(a=10,b=30)
print(w)
