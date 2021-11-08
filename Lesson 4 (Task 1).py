import random
r = random.randint(1,10)

guess = int(input("Guess a number between 1 & 10: "))

while guess != r:
    if guess < r:
        print("Hint: Guess Higher. Try again!")
        guess = int(input("Guess the number: "))

    else:
        print("Hint: Guess lower. Try again!")
        guess = int(input("Guess the number: "))

print("Congratulations, You Win!")




