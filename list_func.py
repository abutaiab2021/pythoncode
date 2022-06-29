from pickle import POP


l=[10,20,30,40,50]
print(l)
print()


# del l[0]
# print(l)

# print(l.pop(1))
# print(l)

# l.remove(50)
# print(l)

# l.clear()
# print(l)

# for value update in list
# l[0]=30
# print(l)

# for value insert in list
# l.insert(0,10)
# print(l)


# l.append(55)
# print(l)

# for nested list create kore append
# n=[10,20,30]
# m=[40,50,60]
# n.append(m)
# print(n)

n=[10,20,30]
m=[40,50,60]
n.extend(m)
print(n)