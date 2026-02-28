n = [1, 2, 8, 9, 7, 3]
a = len(n)

for i in range(a):
    for j in range(0, a-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]

print("Sorted list in ascending order:")
print(n)
