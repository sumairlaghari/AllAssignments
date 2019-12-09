def func(string):
    upper=0
    lower=0
    for c in string:
        if c.isupper():
            upper=upper+1
        elif c.islower():
            lower=lower+1

    print("Upper Case:",upper)
    print("Lower Case:",lower)


string=input("Enter any string: ")
func(string)