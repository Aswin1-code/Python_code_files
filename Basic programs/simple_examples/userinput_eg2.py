height1=170
height2=(height1//2.54)
print(height2)

height1=170
height2="{:0.2f}".format(height1/2.54)
print(height2)

#for getting 2 inputs at a time
a, b=int(input("Enter num1 :")),int(input("Enter num2 :"))
print("Sum is = ", a+b)

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
