N = int(input())

a = list(map(int, input().split()))

if N > 1:
    result = [a[-1]] + a[:-1]
else:
    result = a

print(*result)
