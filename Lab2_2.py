A = int(input("Введите число A: "))
B = int(input("Введите число B (B > A): "))

sum_squares = 0

for num in range(A, B + 1):
    sum_squares += num ** 2

print(f"Сумма квадратов чисел от {A} до {B}: {sum_squares}")