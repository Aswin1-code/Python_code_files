def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Compute the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a



#======================
# Import the user-defined module
import math_utils

def main():
    # Demonstrate the factorial function
    num = 5
    print(f"Factorial of {num}: {math_utils.factorial(num)}")

    # Demonstrate the is_prime function
    num = 29
    print(f"Is {num} a prime number? {'Yes' if math_utils.is_prime(num) else 'No'}")

    # Demonstrate the gcd function
    a, b = 56, 98
    print(f"GCD of {a} and {b}: {math_utils.gcd(a, b)}")

if __name__ == "__main__":
    main()