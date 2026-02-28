name="lamborghini"

#USING INDEXING method for slicing the given string
# name_of_string[start:stop:step

print(name[1])
print(name[0:4])
print(name[:4])    #from beginning to 4th position (but 4th position is not included) 
                   #,,, it will give the same output as like before 
print(name[6:11])  #beginning from 6 position it will print upto 11th position(11th position is not included)
                   #print(name[11])  ----> try this
print(name[6:])    #from 6th position to till the last position
print(name[0:10:1])

print(name[::-1])  #used to reverse a string( print the string from the reverse)
print(name[0::])
print(name[:2:])


#USING slice() function
x=slice(2,-2)       #instead of colon we are using comma and slice function
print(name[x])

x=slice(0,11) 
print(name[x])