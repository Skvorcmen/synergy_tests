num = int(input())

if num % 2 == 0:
    if num > 0:
        print("положительное четное число")
    elif num < 0:
        print("отрицательное четное число")
    else:
        print("нулевое число")
else:
    print("число не является четным")
