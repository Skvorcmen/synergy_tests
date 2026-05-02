A = int(input())
B = int(input())

even = []

for i in range(A, B + 1):
    if i % 2 == 0:
        even.append(str(i))

print(" ".join(even))
