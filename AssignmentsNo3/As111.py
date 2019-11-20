#SMIT/19/PY/B2/08727 PY08727 SUMAIR AIJAZ aliasadzaidi123@gmail.com

num1=int(input("Enter First Number: "))
num2=int(input("Enter 2nd Number: "))

print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Power")
choice=int(input("Enter your choice[1/5]: "))

if choice == 1:
    print(num1+num2)

elif choice == 2:
    print(num1-num2)

elif choice == 3:
    print(num1*num2)

elif choice == 4:
    print(num1/num2)

elif choice == 5:
    print(num1**num2)

else:
    print("wrong choice please choose again")

