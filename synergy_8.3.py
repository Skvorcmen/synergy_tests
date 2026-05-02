m = int(input())
n = int(input())
weight = [int(input()) for _ in range(n)]

weight.sort()
left, right = 0, n - 1
boats = 0

while left <= right:
    if weight[left] + weight[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    boats += 1

print(boats)
