def validate(type_=str, max_length=15,  contains=['05']):
  def inner(func):
    def wrapper(value, *args, **kwargs):


        if type_ == str:
            print(True)
        else:
            print("Should be string!")


        if len(value) > max_length:
            raise ValueError("Please consider Max length!")

        if '05' not in value:
            raise ValueError("Does not contain required sub-string")



        return func(value, *args, **kwargs)
    return wrapper
  return inner

@validate(type_=str, max_length=15, contains=['05'])
def greet(name):
    print("Welcome, {name}!".format(name=name))

#greet("Sana")
#greet("to Python Programming")
#greet("you")
#greet('johndoe05@gmail.com')
greet('johndoe@gm')
