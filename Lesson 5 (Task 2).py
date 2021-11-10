import random
list1 = random.sample(range(1, 10), 9)
print("List 1: ", list1)
list2 = random.sample(range(1, 10), 9)
print("List 2: ", list2)

list1_as_set = set(list1)
intersection = list1_as_set.intersection(list2)


intersection_as_list = list(intersection)

while True:
    print("Common list:" , intersection_as_list)
    break