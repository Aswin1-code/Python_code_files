print("Shallow method to copy")
cities=["madurai","chennai","karur","cuddalore"]
TN=cities     #----> this is not the good way to copy.. this is called SHALLOW copy
a=["car","bus","lorry"]
K=["banglore","mysore",a]
AP=["trupathi","guntur"]
Ind=[TN,AP,K]

print(Ind)
print(Ind[1])      #1D list
print(Ind[0][3])   #2D list
print(Ind[2][2][0]) #--> 3D list

#another method to copy  #Alternate Way
print("\n\t**Alternate Way 1")
cities=["madurai","chennai","karur","cuddalore"]
TN=cities[:]
cities.append('Tanjore')
print(cities)
print(TN)

print("\n\t**Alternate Way 2")
cities=["madurai","chennai","karur","cuddalore"]
TN=cities.copy()
cities.append('Tanjore')
print(cities)
print(TN)

print("\n")
Ind_st=Ind[:]
Ind[0][0]='namakal'
print(Ind[0][0]+'\n')

#Better way to copy is by **deepcopy()
import copy
TN=copy.deepcopy(cities)
print(TN)







 