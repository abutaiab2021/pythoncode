marks = int(input("Enter a number:"))
if(marks > 90):
    print("Excelent")
elif(marks < 90 and marks >= 75):
    print("Very Good")
elif(marks < 75 and marks >= 60):
    print("good")
else:
    print("average")
