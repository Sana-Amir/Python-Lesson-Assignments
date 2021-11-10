word = input("Please enter a word:")
list_of_letters = list(word)
print(list_of_letters)

import random
input_string = "hello"
length_input_string = len(input_string)
i = 1
while i <= length_input_string:
    print(random.choice(input_string), end = '')
    i += 1

