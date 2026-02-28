'''
a=str(input("Enter a string :"))
if a[::-1]==a[0::]:
    print("palindrome")
else :
    print("not")
    
'''
def print_right_palindrome_triangle(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print the first half of the row
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print the second half of the row
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        # Move to the next line
        print()

# Example usage
n = 5
print_right_palindrome_triangle(n)

