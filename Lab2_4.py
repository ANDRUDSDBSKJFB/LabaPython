arr = [int(input(f"Элемент {i + 1}: ")) for i in range(8)]

for i in range(8):
    if arr[i] < 15:
        arr[i] *= 2  # заменяем на удвоенное значение

print("Преобразованный массив:", arr)


n = int(input("Введите длину массива: "))
D = [int(input(f"D[{i}]: ")) for i in range(n)]

sum_odd_indices = sum(D[1::2])  # сумма элементов с нечетными индексами (1, 3, 5, ...)

print("Массив D:", D)
print("Сумма элементов с нечётными индексами:", sum_odd_indices)