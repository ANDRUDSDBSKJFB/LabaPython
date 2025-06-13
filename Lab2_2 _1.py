n = int(input("Введите количество чисел: "))
numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]

sum_even = 0
i = 0

while i < len(numbers) and numbers[i] % 2 == 0:
    sum_even += numbers[i]
    i += 1

print(f"Сумма первых подряд идущих четных чисел: {sum_even}")