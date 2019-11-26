from random import randint

a=randint(1,30)
i=0

while(i!=3):
    guess=int(input("Guess the hidden number: "))

    if guess!=a:
        if a>guess:
            print("Hint: Hidden value is greater then the input value")
        elif a<guess:
            print("Hint: Hidden value is less then the input value")

    if guess!=a and i==2:
        print("you failed to guess the hidden number\nThe Hidden number was",a)

    elif guess==a:
        print("you guessed it right")
        break
    i=i+1
