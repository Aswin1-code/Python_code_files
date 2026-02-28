val1=["chennai","salem","madurai","sivakasi","calicut"]
val2=[3,5,2,1,6,7]
val3=[3,"madurai",4,89,58,"sivakasi","singapore",42,99]

#Accessing list with indexing
print(val2[0])
print(val2[1:4])
print(val2[-2])
print(val2[-2:2])
print(val2[::-1]) # to reverse the given string "|cities|"
print(val2[::2])
print(val2[0:3:2])

#modify
val2[1]="Dubai"
print(val2)

#append
val2.append("Karur")
print(val2)

#insert
val2.insert(2,"puducherry")
print(val2)

#remove using pop()
print(val1)
deleted=val1.pop()
print(deleted+" has been deleted")
print(val1)

#remove by value
print(val2)
val_del=2
print(val2.index(val_del))   #to find index of a character
val2.remove(val_del)
print(val2)

print(val2)
#temporary sort
'''     ## A list that contain both integers and alphabets cannnot be sorted ,, it needs some special operations
     print(sorted(val2))   #val2=[3,'Dubai','puducherry',1,6,7,'Karur']
     print(val2)
'''
print(sorted(val1))   #val1=["chennai","salem","madurai","sivakasi","calicut"]
print(val1)

#permanent sort
val1.sort()
  # val2.sort()   A list that contain both integers and alphabets cannnot be sorted ,,
  #it needs some special operations  
print(val1)
print(val2)

#reverse
val1.reverse()
print(val1)

#length
print(len(val1))
print(len(val2))
print(len(val3))

