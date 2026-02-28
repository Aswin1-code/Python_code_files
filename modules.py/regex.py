import re
text = "Hello, world!"
result = re.match(r"Hello", text)
print(result)
print("---------------------------")

text = "Hello, world!"
result = re.search(r"world", text)
print(result)
print("---------------------------")

text = "The rain in Spain falls mainly in the plain."
result = re.findall(r"in", text)
print(result) 
print("---------------------------")

text = "The rain in Spain"
result = re.finditer(r"in", text)
for match in result:
    print(match)
print("---------------------------")

text = "apple,banana,orange"
result = re.split(r",", text)
print(result)
print("---------------------------")

text = "The rain in Spain"
result = re.sub(r"in", "on", text)
print(result)
print("---------------------------")

pattern = re.compile(r"\d+")
text = "There are 123 apples and 456 oranges."
result = pattern.findall(text)
print(result)
print("---------------------------")
