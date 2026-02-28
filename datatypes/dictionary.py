# Creating a sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. keys() - Get all keys
print("Keys:", my_dict.keys())

# 2. values() - Get all values
print("Values:", my_dict.values())

# 3. items() - Get all key-value pairs
print("Items:", my_dict.items())

# 4. get() - Get the value of a specific key
print("Value for key 'a':", my_dict.get('a'))
print("Value for key 'z' (default):", my_dict.get('z', 'Not Found'))

# 5. update() - Update the dictionary with new key-value pairs
my_dict.update({'d': 4, 'e': 5})
print("After update:", my_dict)

# 6. pop() - Remove a key and return its value
removed_value = my_dict.pop('b')
print("Removed value for key 'b':", removed_value)
print("After pop:", my_dict)

# 7. popitem() - Remove and return the last key-value pair
last_item = my_dict.popitem()
print("Last item removed:", last_item)
print("After popitem:", my_dict)

# 8. setdefault() - Get the value of a key, or set it if it doesn't exist
default_value = my_dict.setdefault('f', 6)
print("Value for key 'f':", default_value)
print("After setdefault:", my_dict)

# 9. copy() - Create a shallow copy of the dictionary
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# 10. clear() - Remove all items from the dictionary
my_dict.clear()
print("After clear:", my_dict)


