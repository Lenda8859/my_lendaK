def average_temperature(temperatures):
    """
    Вычисляет среднюю температуру из списка, исключая значения None.

    Args:
    temperatures (list): Список целых чисел или значений None.

    Returns:
    float: Средняя температура округленная до двух знаков после запятой.
    """
    valid_temps = [temp for temp in temperatures if temp is not None]
    average = sum(valid_temps) / len(valid_temps)
    return round(average, 2)


def sort_numbers(*args):
    """
    Сортирует числа на два списка: отрицательные значения по убыванию и неотрицательные по возрастанию.

    Args:
    *args (float or int): Произвольное количество числовых значений.

    Returns:
    tuple: Два списка - первый с отрицательными числами, второй с неотрицательными.
    """
    negatives = sorted([arg for arg in args if arg < 0], reverse=True)
    non_negatives = sorted([arg for arg in args if arg >= 0])
    return (negatives, non_negatives)
print(sort_numbers.__doc__)


def power_iterative(base, exponent):
    """
    Возвращает число, возведенное в степень, используя итеративный метод.

    Args:
    base (int or float): Основание числа.
    exponent (int): Показатель степени.

    Returns:
    int or float: Результат возведения base в степень exponent.
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def power_recursive(base, exponent):
    """
    Возвращает число, возведенное в степень, используя рекурсивный метод.

    Args:
    base (int or float): Основание числа.
    exponent (int): Показатель степени.

    Returns:
    int or float: Результат возведения base в степень exponent.
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power_recursive(base, -exponent)
    else:
        half_power = power_recursive(base, exponent // 2)
        if exponent % 2 == 0:
            return half_power * half_power
        else:
            return base * half_power * half_power

print()
"""# Пример использования:
temps = [25, 30, None, 28, 22, None, 24]
print("Средняя температура:", average_temperature(temps))

negatives, non_negatives = sort_numbers(-3, 0, 8, -1, 5, -2)
print("Отрицательные числа:", negatives)
print("Неотрицательные числа:", non_negatives)

print("Возведение в степень (итеративно):", power_iterative(2, 5))
print("Возведение в степень (рекурсивно):", power_recursive(2, 5))"""