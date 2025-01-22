import math


def area_of_triangle(a, b, c):
    # Вычисляем полупериметр
    s = (a + b + c) / 2
    # Вычисляем площадь по формуле Герона
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def are_triangles_equal_area(sides1, sides2):
    # Извлекаем стороны треугольников
    a1, b1, c1 = sides1
    a2, b2, c2 = sides2

    # Вычисляем площади
    area1 = area_of_triangle(a1, b1, c1)
    area2 = area_of_triangle(a2, b2, c2)

    # Сравниваем площади
    if math.isclose(area1, area2):
        return True
    else:
        return False


# Пример использования
sides_triangle1 = (3, 4, 5)  # Стороны первого треугольника
sides_triangle2 = (6, 8, 10)  # Стороны второго треугольника

if are_triangles_equal_area(sides_triangle1, sides_triangle2):
    print("Треугольники равновелики.")
else:
    print("Foul!!!")