#to print multiples of 20 greater than or equal to given n
num=''
while not num.isnumeric():
    num=input("Enter a number :")
a=20
print("20")
while a<=int(num):
    a+=20
    print(a)
