def is_prime(num):
    if num < 2:
        return "Not a prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not a prime"
    return "prime"
while 1:
    print(is_prime(int(input("Enter a number: ")))) 
