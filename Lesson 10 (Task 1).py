class Person:
  def __init__(self, fname , lname ,age):
    self.fname = fname
    self.lname = lname
    self.age = age


  def myfunc(self):
    print("Hello, My name is " + self.fname + " "+ self.lname + " and my age is " + str(self.age))

p1 = Person("Sana","Amir", 23)
p1.myfunc()
