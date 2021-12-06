
class MyNum:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError("Incorrect operand")
        return MyNum(self.value + other.value)

    def __str__(self):
        return f"<MyNum: {self.value}>"

    def __repr__(self):
        return self.__str__()

x = MyNum(1)
y = MyNum(2)

print(x + y)