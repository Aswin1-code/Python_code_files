#break

print("\tSeparate odd and even numbers from the list\n")
print("Enter a list of numbers.Press z to end")
odd=[]
even=[]
while True:
    inp=input()
    if inp=='z':
       break
    if int(inp)%2==0:
       even.append(int(inp))
    else:
       odd.append(int(inp))
print("odd = "+str(odd))
print("even = "+str(even)) 

#continue
'''
str1="A,B,C,D,E"
str2=''
for i in str1:          
    if i==',':          
        continue        
    str2=str2+i         
print(str2)
'''
'''
#pass
str1="A,B,C,D,E"
str2=''
for i in str1:           #alternate code
    if i==',':           # #alternate code
        pass             #  if i!=',': 
    else:                #     str2=str2+i    
        str2=str2+i      # print(str2)
print(str2)
'''