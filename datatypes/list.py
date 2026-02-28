# Creating a sample list
my_list = [1, 2, 3, 2, 4, 2, 5]

# 1. append() - Add an element to the end of the list
my_list.append(6)
print("After append(6):", my_list)

# 2. extend() - Add multiple elements to the end of the list
my_list.extend([7, 8])
print("After extend([7, 8]):", my_list)

# 3. insert() - Insert an element at a specific position
my_list.insert(2, 10)  # Insert 10 at index 2
print("After insert(2, 10):", my_list)

# 4. remove() - Remove the first occurrence of a specific value
my_list.remove(2)  # Remove the first occurrence of 2
print("After remove(2):", my_list)

# 5. pop() - Remove and return an element at a specific index (default is the last element)
popped_element = my_list.pop()
print("After pop():", my_list, "| Popped element:", popped_element)

# 6. index() - Get the index of the first occurrence of a specific value
index_of_3 = my_list.index(3)
print("Index of 3:", index_of_3)

# 7. count() - Count the occurrences of a specific value
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

# 8. reverse() - Reverse the order of the list
my_list.reverse()
print("After reverse():", my_list)

# 9. sort() - Sort the list in ascending order
my_list.sort()
print("After sort():", my_list)

# 10. clear() - Remove all elements from the list
my_list.clear()
print("After clear():", my_list)