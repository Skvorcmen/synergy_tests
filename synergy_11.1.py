def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


num = int(input("Введите натуральное целое число: "))

fact_num = factorial(num)
print(f"Факториал числа {num} = {fact_num}")

factorials_list = []
for i in range(fact_num, 0, -1):
    factorials_list.append(factorial(i))

print(f"Список факториалов: {factorials_list}")
