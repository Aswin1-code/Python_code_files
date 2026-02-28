'''n=[]
for i in range(1500,1700+1):
    if i%7==0 and i%5==0:
        n.append(i)
print(n)

n=int(input("Enter a no: "))
l=1
for i in range(l,n+1):
    print(" "*(n-i),"* "*i)
for j in range(n-1,l-1,-1):
    print(" "*(n-j),"* "*j)

import math
isprime=True
n=int(input("Enter no: "))
for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
        isprime=False
        break
if isprime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")'''

'''
n=int(input("Enter range: "))
fib,j=[0,1],1
for i in range(2,n+1):
    if fib[-1]<=n:
        j+=1
        fib.append(fib[-1]+fib[-2])
print(fib[:j])'''

n=int(input("Enter range: "))
fib,j=[0,1],1
while fib[-1]<n:
    j+=1
    fib.append(fib[-1]+fib[-2])
print(fib[:j])
    

'''n=str(input("Enter nos: "))
l=n.split(',')
res=[]
for i in l:
    if int(i,2)%5==0:
        res.append(i)
print(res)'''