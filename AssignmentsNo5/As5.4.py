def func(string):
    str=''
    for i in range(len(string)-1,-1,-1):
        str=str+string[i]

    if str == string:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

string=input("Enter any word: ")
func(string)