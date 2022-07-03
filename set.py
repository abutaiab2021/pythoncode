# set1 = set()

# set2 = {"Abu", 2, 3, "Taiab"}

# print(type(set1))
# print(set2)

# set1.add("Malek")
# set1.add(60)
# set2.add(50)
# print(set1)
# print(set2)

# set2.remove(2)
# print(set2)


s={10,20,30,40}
print(s)

for a in s:
    print(a)

add = s.add(50)
print(s)

pop=s.pop()
print(s)

remove=s.remove(20)
print(s)

# clear=s.clear()
# print(s)

discard=s.discard(30)
print(s)


u={20,30,40,60}
update=s.update(u)
print(s)