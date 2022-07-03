student={
    "Alhaj":{"name":"Alhaj","Age":28,"salary":15000},
    "Kasem":{"name":"Kasem","Age":30,"salary":20000},
    "Hasem":{"name":"Hasem","Age":33,"salary":30000}
}

print(student)
print(student["Alhaj"]["Age"])
print()


for a in student.get("Kasem") :
    print(a)
print()
for k,v in student.items():
    print(k,v["Age"],v["salary"])