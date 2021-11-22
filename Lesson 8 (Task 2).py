a = input("Input a: ")
b = input("Input b: ")

try:
    a = int(a)
    x = a**2
    b = int(b)
    print(x / b)

except:
    if type(a) is not int and type(b) is not int:
        print("Only integers are allowed!")
    if b == 0:
        print("Numbers can not be divided by 0!")
