def replace_p_with_stars(s):
    n = len(s)  # Получаем длину строки
    half_n = n // 2  # Вычисляем половину длины строки

    # Заменяем 'п' на '*' в первой половине строки
    first_half = s[:half_n].replace('п', '*')
    second_half = s[half_n:]  # Вторая половина строки остается без изменений

    # Объединяем обе половины
    transformed_string = first_half + second_half
    return transformed_string

# Пример использования
input_string = input("Введите строку: ")
result = replace_p_with_stars(input_string)
print("Преобразованная строка:", result)
