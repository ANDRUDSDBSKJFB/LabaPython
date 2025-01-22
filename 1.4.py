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
