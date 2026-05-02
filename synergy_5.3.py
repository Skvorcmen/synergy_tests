min_sum = int(input("минимальная сумма: "))
mike = int(input("долларов у Майкла: "))
ivan = int(input("долларов у Ивана: "))

if mike >= min_sum and ivan >= min_sum:
    print(2)
elif mike >= min_sum and ivan < min_sum:
    print("Mike")
elif ivan >= min_sum and mike < min_sum:
    print("Ivan")
elif mike + ivan >= min_sum:
    print(1)
else:
    print(0)
