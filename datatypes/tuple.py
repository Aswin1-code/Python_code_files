# Creating a sample tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5)

# 1. count() - Count occurrences of a specific value
count_of_2 = my_tuple.count(2)
print("Count of 2 in tuple:", count_of_2)

# 2. index() - Find the first index of a specific value
index_of_3 = my_tuple.index(3)
print("Index of 3 in tuple:", index_of_3)

# 3. len() - Get the length of the tuple
length = len(my_tuple)
print("Length of tuple:", length)

# 4. max() - Get the maximum value in the tuple
max_value = max(my_tuple)
print("Maximum value in tuple:", max_value)

# 5. min() - Get the minimum value in the tuple
min_value = min(my_tuple)
print("Minimum value in tuple:", min_value)

# 6. sum() - Get the sum of all elements in the tuple
sum_of_elements = sum(my_tuple)
print("Sum of elements in tuple:", sum_of_elements)

# 7. sorted() - Return a sorted list of the tuple's elements
sorted_tuple = sorted(my_tuple)
print("Sorted tuple (as list):", sorted_tuple)

# 8. any() - Check if any element in the tuple is truthy
any_truthy = any(my_tuple)
print("Is any element truthy in tuple?:", any_truthy)

# 9. all() - Check if all elements in the tuple are truthy
all_truthy = all(my_tuple)
print("Are all elements truthy in tuple?:", all_truthy)

# 10. tuple() - Convert an iterable into a tuple
list_to_convert = [10, 20, 30]
converted_tuple = tuple(list_to_convert)
print("Converted tuple from list:", converted_tuple)