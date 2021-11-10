x = []
y = []

i=1
while i <= 100:
    x.append(i)
    i+=1

print("List 1: ", x)

i=0
while i < len(x):
    if x[i]%7 == 0 and x[i]%5!=0:
     y.append(x[i])

    i+=1

print("Filtered list: ", y)