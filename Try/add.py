str="1,2,3,4,5"
l=[]
for i in str:
    if i!=',':
        l.append(int(i))
print(l)
print(tuple(l))