num = int(input())

d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10

result = (d4**d5) * d3 / (d1 - d2)

print(result)
