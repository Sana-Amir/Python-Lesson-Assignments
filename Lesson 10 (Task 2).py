class Dog:
  age_factor = 7
  def __init__(self, dogage):
    self.dogage = dogage

#hage stands for human-age
  def human_age(self, hage):
    self.hage = hage

#returns the dog’s age in human equivalent
  def age(self):
    return self.dogage * 7

# human age is 7 and dog age is 1
p1 = Dog(7)
print("Human age equivalent to Dog age : ", p1.age())

