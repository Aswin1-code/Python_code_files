name="aSwIn"
age=18
print("Hi "+ name.upper() + " you are " + str(age) + " old")
name="ASWIN's"
print("Lower-- " + name.lower())
name='"aswin"'
print("Upper-- "+ name.upper())

message="Happy birthday"

print("length -- "+ str(len(message)))
print(message.find("a")) 
'''as the count of places will start from 0,1,2,,, 
   it gives the position of "a" as 1 eventhough its position is 2
   so we are adding "1" to it 
'''
b=int(message.find("a"))
print(b+1)    #increment the position by 1

print("count of letter 'h' is "+ str(message.count("h")))

#for replacing the string
Ex="good123"
print(Ex.replace("oo","o")) 
print("care".replace("re","r")) #we can also do without assigning before
ex="God"
print(ex.isalpha()) #if assigned string is alphabet , it will return "true" otherwise "false"
print(ex.isdigit()) #similarly if its a digit ,, do similar work as like isalpha 
print(Ex.isalnum()) #return "true" when it is both alphabet as well as numeric
