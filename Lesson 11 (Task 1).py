class Person:
    def __init__(self, f_name, l_name, age=16):
        if age is None or age < 0:
            raise ValueError("Age should be a positive integer")

        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def get_full_name(self):
        return f"{self.f_name}{self.l_name}"

class Student(Person):
    def __init__(self, f_name, l_name, course, age=16):
        if age is None or age < 0:
            raise ValueError("Age should be a positive integer")

        self.f_name = f_name
        self.l_name = l_name
        self.age = age

        self.course = course

    def is_studying(self, course):
        return self.course

    #def get_full_name(self):
     #   return f"{self.f_name}{self.l_name}"

class Teacher(Person):
    def __init__(self, f_name, l_name, courses, salary, age=50):
        if age is None or age < 0:
            raise ValueError("Age should be a positive integer")

        self.f_name = f_name
        self.l_name = l_name
        self.age = age

        self.salary = salary

    def is_salary(self, salary):
        return salary

    #def get_full_name(self):
    #   return f"{self.f_name}{self.l_name}"

#Sana Amir
sana = Student("Sana ", "Amir", "Python")
print(sana.get_full_name())
print("{} is studying {}.".format(sana.f_name, sana.is_studying("Python")))

#Anna Amir
anna = Student("Anna ", "Amir", "JS")
print(anna.get_full_name())
print("{} is studying {}.".format(anna.f_name, anna.is_studying("JS")))


#Ayesha Ch
ayesha = Teacher("Ayesha ", "Ch", ["Python", "JS"], 50000, age=50)
print(ayesha.get_full_name())
print("{}is a teacher and her salary is {}.".format(ayesha.f_name, ayesha.is_salary("SEK 50,000")))


