import math

def calculate_hypotenuse(a, b):
    """Вычисляет гипотенузу по двум катетам."""
    return math.sqrt(a**2 + b**2)

# Ввод данных для первого треугольника
a1 = float(input("Введите первый катет первого треугольника: "))
b1 = float(input("Введите второй катет первого треугольника: "))

# Ввод данных для второго треугольника
a2 = float(input("Введите первый катет второго треугольника: "))
b2 = float(input("Введите второй катет второго треугольника: "))

# Вычисление гипотенуз
hypotenuse1 = calculate_hypotenuse(a1, b1)
hypotenuse2 = calculate_hypotenuse(a2, b2)

# Сравнение гипотенуз
if hypotenuse1 > hypotenuse2:
    print(f"Гипотенуза первого треугольника ({hypotenuse1:.2f}) больше, чем второго ({hypotenuse2:.2f})")
elif hypotenuse1 < hypotenuse2:
    print(f"Гипотенуза второго треугольника ({hypotenuse2:.2f}) больше, чем первого ({hypotenuse1:.2f})")
else:
    print(f"Гипотенузы равны ({hypotenuse1:.2f})")






    def fibonacci(k):
        if k == 1 or k == 2:
            return 1
    
    return fibonacci(k - 1) + fibonacci(k - 2)

k = int(input("Введите номер члена последовательности Фибоначчи (k ≥ 1): "))

if k < 1:
    print("Ошибка: k должно быть ≥ 1")
else:
    print(f"F({k}) = {fibonacci(k)}")