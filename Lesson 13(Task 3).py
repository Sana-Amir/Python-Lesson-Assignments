def choose_func(nums, func1, func2):
 is_all_positive = True
 for num in nums:
  if num < 0:
   is_all_positive = False
   break

 if is_all_positive:
  return func1(nums)

 return func2(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
 return [num ** 2 for num in nums]

def remove_negatives(nums):
 return [num for num in nums if num > 0]


#assert choose_func(nums1, square_nums, remove_negatives)
#assert choose_func(nums2, square_nums, remove_negatives)
print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

