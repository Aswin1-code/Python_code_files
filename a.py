#3
def sumAll(d):
    s=0
    for val in d.values():
        s+=val
    print(f"New dictionary: {d}")
    print(f"sum of values: {s}")
l=[i for i in range(1,int(input("Enter range: "))+1)]
d={}
for i in l:
    d[i]=i**2
sumAll(d)

######
#2
d1,d2={},{}
n1=int(input("Enter no. of pairs 1: "))
while (n1>0):
    key=input("key: ")
    val=input("Val: ")
    d1[key]=val
    n1-=1
n2=int(input("Enter no. of pairs 2: "))
while (n2>0):
    key=input("Key: ")
    val=input("Val: ")
    d2[key]=val
    n2-=1
merged={**d1,**d2}
print(f"{merged} : merged dictionary")

#####
#1
def newPair(k,v,d):
    d[k]=v
    sort2=dict(sorted(d.items(),key=lambda item:item[0],reverse=True))
    print(f"Desc order: {sort2}")
    
n=int(input("No. of pairs: "))
d={}
while n>0:
    ke=int(input("Key: "))
    v=int(input("Val: "))
    d[ke]=v
    n-=1
sort1=dict(sorted(d.items(),key=lambda item: item[1]))
print(f"Asc order: {sort1}")
k,v=int(input("New Key: ")),int(input("New Val: "))
newPair(k,v,d)

#####
#4
dic1={'a':1,'b':2}
dic2={'c':3,'d':4}
dic1_cp=dic1.copy()
#print(f"Using | : {dic1|dic2}")
UnPacked={**dic1,**dic2}
print(f"Using dictionary unpacking: {UnPacked}")
dic1.update(dic2)
print(f"Using update() :{dic1}")
for key,val in dic2.items():
    dic1_cp[key]=val
print(f"Using for loop: {dic1}")


