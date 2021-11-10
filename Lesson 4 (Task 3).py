import random
x= input("Word: ")
i = 1
while i<=5:
    result = random.choice(x) + random.choice(x) + random.choice(x) + random.choice(x) + random.choice(x)
    print(result)
    i+=1