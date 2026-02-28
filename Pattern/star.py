import re
a="car is good"
print(re.findall(r"\b\w{3}\b",a))
print(re.findall(r"\b\w{3,5}\b",a))