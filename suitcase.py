from random import random

def max_kg_suit(weight, max_total):
   if weight <= max_total:
        return max_total - weight
   else:
        return "Вес чемодана превышает максимально допустимый"


def print_max_kg(max_kilogram):
    if isinstance(max_kilogram, (int, float)):
        print(f'Можно добавить {max_kilogram:.2f} кг к весу чемодана')
    else:
        print(max_kilogram)

try:
    weight = float(input("введите вес вашего чемодана: "))
    max_total = 25

    # Находим максимальное килограмм
    max_kilogram = max_kg_suit(weight, max_total)
    print_max_kg(max_kilogram)

except ValueError:
    print("Ошибка: Введено некорректное значение для веса чемодана.")


