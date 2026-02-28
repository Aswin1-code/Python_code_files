
def sum(n1,n2):
    return (n1+n2)
def mul(n1,n2):
    return (n1*n2)
def div(n1,n2):
    if n1>n2:
        return (n1/n2)
    else:
        return (n2/n1)
def sub(n1,n2):
    return (n1-n2)


def comp(a1,a2,a3):
    if a1>a2:
        if a1>a3:
            return a1
        else:
            return a3
    else:
        if a2>a3:
            return a2
        else:
            return a3


a1,a2,a3=int(input("Enter value1: ")),int(input("Enter value2: ")),int(input("Enter value3: "))
print("{} is greater".format(comp(a1,a3,a3)))

#args
def tot(*a):  #*a or *args or *fg  and variable
    sum=0
    for i in a:
        sum+=i
    return sum
print(tot(1, 2, 3, 4))
print(tot(5,6,7,8,9,5))
print(tot(7,8)) 
print("-----------")

# kwargs
def k(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

# Example usage
k(name="Alice", age=30, city="New York")
k(name="Bob", age=25)
print("----------------------------")


def n(f,l):     #f- fname , l- lname
    print(f+" Hi "+l)
n(f="A",l="B")
n(l="A",f="B")
print("------")

def e(f,l="noName"):       #we can give any default value at last and not at first
    print("hi"+" "+f+" "+l)
e(f="A",l="B")
e(f="C")

def Print_list(list):
    for i in range(0,len(list)):
        print(list[i].title())
        
        
names=["ab","bc","cd"]
Print_list(names)        #names   -> send as original string to function
#Print_list(names[:])   #names[:] ->send as separate string and so no modification in original string
print("--")    
print(names)

def Print_list(list):
    for i in range(0, len(list)):
        print(list[i].title())

names = ["ab", "bc", "cd"]
#Print_list(names)        # names -> send as original string to function
Print_list(names[:])   # names[:] ->send as separate string and so no modification in original string
print("--")
print(names) 