print("Example program for nestedif")
print("To find quotient is odd or even")
num1=str(input("Enter a number"))
num2=str(input("Enter another number"))
if int(num1)>int(num2):
    print(num1 +" is greater than "+ num2)
    b=int(num1)/int(num2)
    if b%2==0:
        print("Quotient is even number")
    else:
        print("Quotient is odd number")
elif int(num1)<int(num2) :
    print(num1 +" is lesser than "+ num2)
    b=int(num2)/int(num1)
    if b%2==0:
        print("Quotient is even number")
    else:
        print("Quotient is odd number")
else:
    print("Thank you\n Bye!!!")