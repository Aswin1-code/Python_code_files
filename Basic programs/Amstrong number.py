num = int(input("Enter a number: "))
is_armstrong = num == sum(int(digit) ** len(str(num)) for digit in str(num))
print(f"{num} is an Armstrong number." if is_armstrong else f"{num} is not an Armstrong number.")
