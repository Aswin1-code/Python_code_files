def arithmetic_sequence(a, d, n):
    """Generate an arithmetic sequence."""
    return [a + d * i for i in range(n)]

def geometric_sequence(a, r, n):
    """Generate a geometric sequence."""
    return [a * r**i for i in range(n)]

def harmonic_sequence(n):
    """Generate a harmonic sequence."""
    return [1 / (i + 1) for i in range(n)]

def fibonacci_sequence(n):
    """Generate Fibonacci sequence."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def juggler_sequence(n):
    """Generate Juggler sequence."""
    jug = [1]  # Starting with the first term
    while len(jug) < n:
        next_term = jug[-1]**0.5 if jug[-1] % 2 == 0 else 3 * jug[-1] + 1
        jug.append(int(next_term))
    return jug

def padovan_sequence(n):
    """Generate Padovan sequence."""
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    pad = [1, 1, 1]
    for i in range(3, n):
        pad.append(pad[-2] + pad[-3])
    return pad[:n]

def aliquot_sequence(n):
    """Generate Aliquot sequence."""
    seq = [n]
    while n > 0:
        n = sum(i for i in range(1, n) if n % i == 0)
        seq.append(n)
    return seq


def stern_brocot_sequence(n):
    """Generate Stern-Brocot sequence."""
    stern = []
    left, right = 0, 1
    for _ in range(n):
        num = left + right
        stern.append(num)
        left = right
        right = num
    return stern

def newman_conway_sequence(n):
    """Generate Newman-Conway sequence."""
    if n < 1:
        return []
    if n == 1:
        return [1]
    
    p = [0] * (n + 1)
    p[1], p[2] = 1, 1
    for i in range(3, n + 1):
        p[i] = p[p[i - 1]] + p[i - p[i - 1]]
    return p[1:]

def sylvester_sequence(n):
    """Generate Sylvester’s sequence."""
    sylvester = [1]
    for i in range(1, n):
        sylvester.append(sylvester[i - 1] + 1)
        sylvester[i] = sylvester[i - 1] * sylvester[i] // sylvester[i - 1]
    return sylvester

def recaman_sequence(n):
    """Generate Recaman’s sequence."""
    recaman = [0]
    seen = {0}
    for i in range(1, n):
        next_val = recaman[i - 1] - i
        if next_val > 0 and next_val not in seen:
            recaman.append(next_val)
        else:
            recaman.append(recaman[i - 1] + i)
        seen.add(recaman[i])
    return recaman

# Example usage of all the sequences
n = 10  # Number of terms to generate

print("Arithmetic Sequence (a=1, d=2):", arithmetic_sequence(1, 2, n))
print("Geometric Sequence (a=2, r=3):", geometric_sequence(2, 3, n))
print("Harmonic Sequence:", harmonic_sequence(n))
print("Fibonacci Sequence:", fibonacci_sequence(n))
print("Juggler Sequence:", juggler_sequence(n))
print("Padovan Sequence:", padovan_sequence(n))
print("Aliquot Sequence (starting from 12):", aliquot_sequence(12))
print("Stern-Brocot Sequence:", stern_brocot_sequence(n))
print("Newman-Conway Sequence:", newman_conway_sequence(n))
print("Sylvester's Sequence:", sylvester_sequence(n))
print("Recaman’s Sequence:", recaman_sequence(n))
