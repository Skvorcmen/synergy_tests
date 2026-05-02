X = int(input())

count = 0
d = 1

while d * d <= X:
    if X % d == 0:
        if d * d == X:
            count += 1
        else:
            count += 2
    d += 1

print(count)
