# 1. Fibonacci Series
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# 2. Lucas Numbers
def lucas(n):
    if n == 0:
        return [2]
    if n == 1:
        return [2, 1]
    luc = [2, 1]
    for i in range(2, n):
        luc.append(luc[-1] + luc[-2])
    return luc[:n]

# 3. Triangular Numbers
def triangular(n):
    return [i * (i + 1) // 2 for i in range(n)]

# 4. Tetrahedral Numbers
def tetrahedral(n):
    return [(i * (i + 1) * (i + 2)) // 6 for i in range(n)]

# 5. Pell Numbers
def pell(n):
    pell_nums = [0, 1]
    for i in range(2, n):
        pell_nums.append(2 * pell_nums[-1] + pell_nums[-2])
    return pell_nums[:n]

# 6. Catalan Numbers
from math import comb
def catalan(n):
    return [comb(2 * i, i) // (i + 1) for i in range(n)]

# 7. Mersenne Numbers
def mersenne(n):
    return [2**i - 1 for i in range(n)]

# 8. Power Series (x^n)
def power_series(x, n):
    return [x**i for i in range(n)]

# 9. Arithmetico-Geometric Series
def arithmetico_geometric(a, d, r, n):
    series = []
    term = a
    for i in range(n):
        series.append(term)
        a += d
        term *= r
    return series

# 10. Square Numbers
def square_numbers(n):
    return [i**2 for i in range(n)]

# 11. Cube Numbers
def cube_numbers(n):
    return [i**3 for i in range(n)]

# 12. Factorial Numbers
from math import factorial
def factorial_numbers(n):
    return [factorial(i) for i in range(n)]

# 14. Fermat Numbers
def fermat_numbers(n):
    return [2**(2**i) + 1 for i in range(n)]

# 15. Fibonacci Prime Numbers
def fib_prime(n):

    from sympy import isprime
    fib_primes = []
    count, i = 0, 0
    while count < n:
        fib_num = fibonacci(i)[-1]
        if isprime(fib_num):
            fib_primes.append(fib_num)
            count += 1
        i += 1
    return fib_primes

# 16. Oscillating Fibonacci Numbers
def oscillating_fibonacci(n):
    return [(-1)**i * fibonacci(i)[-1] for i in range(n)]

# 17. Arithmetic Series
def arithmetic_series(a, d, n):
    return [a + i * d for i in range(n)]

# 18. Geometric Series
def geometric_series(a, r, n):
    return [a * (r**i) for i in range(n)]

# 19. Harmonic Numbers
def harmonic_numbers(n):
    return [sum(1 / i for i in range(1, k + 1)) for k in range(1, n + 1)]

# 20. Conway's Constant Sequence
def conways_constant(n):
    return [round(1.303577269034296 * i) for i in range(n)]

# 21. Bell Numbers
def bell_number(n):
    bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bell[0][0] = 1

    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

    return [bell[i][0] for i in range(n)]

# 22. Lazy Caterer's Sequence
def lazy_caterer(n):
    return [(i * (i + 1)) // 2 + 1 for i in range(n)]

# 23. Padovan Sequence
def padovan(n):
    pad = [1, 1, 1]
    for i in range(3, n):
        pad.append(pad[-2] + pad[-3])
    return pad[:n]

# 24. Tribonacci Numbers
def tribonacci(n):
    trib = [0, 0, 1]
    for i in range(3, n):
        trib.append(trib[-1] + trib[-2] + trib[-3])
    return trib[:n]

# 25. (n)th prime numbers
def nth_prime(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        for p in primes:
            if candidate % p == 0:
                break
        else:
            primes.append(candidate)
        candidate += 1
    return primes

# 26. The Sum of the First n Natural Numbers
def sum_natural(n):
    return n * (n + 1) // 2

# 27. The Fibonacci Sequence of Factorials
def fib_factorial(n):
    return [factorial(fibonacci(i)[-1]) for i in range(n)]

# 28. Sum of Squares
def sum_of_squares(n):
    return [sum(i*i for i in range(1, k + 1)) for k in range(1, n + 1)]

# 29. Sum of Cubes
def sum_of_cubes(n):
    return [sum(i**3 for i in range(1, k + 1)) for k in range(1, n + 1)]

# 30. The Decimal Sequence
def decimal_sequence(n):
    return [i for i in range(n)]

# Example usage of all functions
n = 10  # Number of terms to generate
print("1. Fibonacci Series:", fibonacci(n))
print("2. Lucas Numbers:", lucas(n))
print("3. Triangular Numbers:", triangular(n))
print("4. Tetrahedral Numbers:", tetrahedral(n))
print("5. Pell Numbers:", pell(n))
print("6. Catalan Numbers:", catalan(n))
print("7. Mersenne Numbers:", mersenne(n))
print("8. Power Series (x^n) with x=2:", power_series(2, n))
print("9. Arithmetico-Geometric Series (a=1, d=1, r=2):", arithmetico_geometric(1, 1, 2, n))
print("10. Square Numbers:", square_numbers(n))
print("11. Cube Numbers:", cube_numbers(n))
print("12. Factorial Numbers:", factorial_numbers(n))
print("13. Fibonacci Factorial Numbers:", fib_factorial(n))
print("14. Fermat Numbers:", fermat_numbers(n))
print("15. Fibonacci Prime Numbers:", fib_prime(n))
print("16. Oscillating Fibonacci Numbers:", oscillating_fibonacci(n))
print("17. Arithmetic Series (a=1, d=1):", arithmetic_series(1, 1, n))
print("18. Geometric Series (a=1, r=2):", geometric_series(1, 2, n))
print("19. Harmonic Numbers:", harmonic_numbers(n))
print("20. Conway's Constant Sequence:", conways_constant(n))
print("21. Bell Numbers:", bell_number(n))
print("22. Lazy Caterer's Sequence:", lazy_caterer(n))
print("23. Padovan Sequence:", padovan(n))
print("24. Tribonacci Numbers:", tribonacci(n))
print("25. nth Prime Numbers:", nth_prime(n))
print("26. Sum of the First n Natural Numbers:", sum_natural(n))
print("27. Sum of Squares:", sum_of_squares(n))
print("28. Sum of Cubes:", sum_of_cubes(n))
print("29. Decimal Sequence:", decimal_sequence(n))
