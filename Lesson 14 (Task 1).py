a = (2,3)
def my_decorator(func):
    def wrapper():
        print("2 + 3 =", sum(a))
        func()
        print("2 ** 3= ", pow(2,3))

    return wrapper()

@my_decorator
def lets_change():
    print("Lets change it a bit!")



