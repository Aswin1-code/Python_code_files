'''t1=0
t2=1
nextTerm=t1+t2
n=int(input("Enter limiting value :"))
print(t1,end=',')
print(t2,end=',')
for i in range(3,n):
      print(nextTerm,end=',')
      t1 = t2
      t2 = nextTerm
      nextTerm = t1 + t2
    '''
n = int(input("Enter a number: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print(fib[:n])

