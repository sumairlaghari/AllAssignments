age=int(input("Enter your age: "))

if age>0 and age<3:
    print("the ticket is free")
elif age>=3 and age<=12:
    print("the ticket is 10$")
else:
    print("the ticket is 15$")
