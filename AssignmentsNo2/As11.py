#SMIT/19/PY/B2/08727 PY08727 SUMAIR AIJAZ aliasadzaidi123@gmail.com

sub1=int(input("Enter Marks For Subject 1: "))
sub2=int(input("Enter Marks For Subject 2: "))
sub3=int(input("Enter Marks For Subject 3: "))
sub4=int(input("Enter Marks For Subject 4: "))
sub5=int(input("Enter Marks For Subject 5: "))

total=sub1+sub2+sub3+sub4+sub5

if sub1>=40 and sub1<=49:
    print("Subject 1 Grade is: 'D'")
elif sub1>=50 and sub1<=59:
    print("Subject 1 Grade is: 'C'")
elif sub1>=60 and sub1<=79:
    print("Subject 1 Grade is: 'B'")
elif sub1>=80:
    print("Subject 1 Grade is: 'A'")
else:
    print("Subject 1 Grade is: 'F'")


if sub2>=40 and sub2<=49:
    print("Subject 2 Grade is: 'D'")
elif sub2>=50 and sub2<=59:
    print("Subject 2 Grade is: 'C'")
elif sub2>=60 and sub2<=79:
    print("Subject 2 Grade is: 'B'")
elif sub2>=80:
    print("Subject 2 Grade is: 'A'")
else:
    print("Subject 2 Grade is: 'F'")


if sub3>=40 and sub3<=49:
    print("Subject 3 Grade is: 'D'")
elif sub3>=50 and sub3<=59:
    print("Subject 3 Grade is: 'C'")
elif sub3>=60 and sub3<=79:
    print("Subject 3 Grade is: 'B'")
elif sub3>=80:
    print("Subject 3 Grade is: 'A'")
else:
    print("Subject 3 Grade is: 'F'")


if sub4>=40 and sub4<=49:
    print("Subject 4 Grade is: 'D'")
elif sub4>=50 and sub4<=59:
    print("Subject 4 Grade is: 'C'")
elif sub4>=60 and sub4<=79:
    print("Subject 4 Grade is: 'B'")
elif sub4>=80:
    print("Subject 4 Grade is: 'A'")
else:
    print("Subject 4 Grade is: 'F'")


if sub5>=40 and sub5<=49:
    print("Subject 5 Grade is: 'D'")
elif sub5>=50 and sub5<=59:
    print("Subject 5 Grade is: 'C'")
elif sub5>=60 and sub5<=79:
    print("Subject 5 Grade is: 'B'")
elif sub5>=80:
    print("Subject 5 Grade is: 'A'")
else:
    print("Subject 5 Grade is: 'F'")

print("Total Marks is:",total)