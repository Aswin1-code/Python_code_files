# Open the file for reading
with open('example.txt', 'r') as file:
    content = file.read()
    print('File Content:')
    print(content)

# Open a file for writing
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a file handling example in Python.\n')

# Append to the file
with open('example.txt', 'a') as file:
    file.write('Appending a new line to the file.\n')

# Read the file line by line
with open('example.txt', 'r') as file:
    print('Reading line by line:')
    for line in file:
        print(line, end='')
#*********************************************************************   
print("*")     
def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
replace_word_in_file('example.txt', 'World', 'Aswin')