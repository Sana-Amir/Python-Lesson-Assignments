class Animal:
    def __init__(self, age= None):
        self.age = age

    def get_age(self):
        return self.age

    def say(self):
        print("What if animals can talk...")

class Cat(Animal):
    def say(self):
        print("Sound of cat: meow meow")

class Dog(Animal):
    def say(self):
        print("Sound of Dog: bow bow")

some_animal = Animal()
some_animal.say()

cat1 = Cat(age=10)
dog1 = Dog(age=20)

print("Age of cat:", cat1.get_age())
print("Age of dog:", dog1.get_age())

cat1.say()
dog1.say()


