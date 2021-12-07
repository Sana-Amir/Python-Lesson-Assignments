def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add


func = test(5)
print(func(4))

"""
STEPS:

test a = 5
a +=1 -> 5+1 = 6 =a
return a+b -> 6+4 = 10

"""