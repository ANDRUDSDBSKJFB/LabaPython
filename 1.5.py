def sum_and_product(arr):
    even_sum = 0  # Сумма элементов с четными номерами
    odd_product = 1  # Произведение элементов с нечетными номерами
    odd_found = False  # Флаг, чтобы проверить, найдены ли нечетные элементы

    for i in range(len(arr)):
        if i % 2 == 0:  # Четный индекс
            even_sum += arr[i]
        else:  # Нечетный индекс
            odd_product *= arr[i]
            odd_found = True  # Установим флаг, если нашли хотя бы один нечетный элемент

    # Если нечетные элементы не найдены, установим произведение в 0
    if not odd_found:
        odd_product = 0

    return even_sum, odd_product

# Пример использования
input_array = [int(x) for x in input("Введите массив целых чисел, разделенных пробелами: ").split()]
even_sum, odd_product = sum_and_product(input_array)
print("Сумма элементов с четными номерами:", even_sum)
print("Произведение элементов с нечетными номерами:", odd_product)

def swap_min_max(arr):
    if len(arr) == 0:
        return arr  # Если массив пустой, возвращаем его

    min_index = arr.index(min(arr))  # Индекс минимального элемента
    max_index = arr.index(max(arr))  # Индекс максимального элемента

    # Переставляем минимальный и максимальный элементы
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

    return arr

# Пример использования
input_array = [int(x) for x in input("Введите массив целых чисел, разделенных пробелами: ").split()]
result_array = swap_min_max(input_array)
print("Массив после перестановки минимального и максимального элементов:", result_array)
