import random
import statistics
import math

# Создаем список из десяти целых чисел
numbers = [10, 25, 6, 45, 32, 8, 17, 30, 21, 4]

# Подсчет суммы чисел списка
total_sum = math.fsum(numbers)

# Вычисление среднего значения
mean_value = statistics.mean(numbers)

# Вычисление медианы
median_value = statistics.median(numbers)

# Вычисление стандартного отклонения
std_dev = statistics.stdev(numbers)

# Вывод результатов
print(f"Список чисел: {numbers}")
print(f"Сумма чисел: {total_sum}")
print(f"Среднее значение: {mean_value}")
print(f"Медиана: {median_value}")
print(f"Стандартное отклонение: {std_dev}")

# Получение случайного числа из списка
random_number = random.choice(numbers)
print(f"Случайное число из списка: {random_number}")

# Получение трех случайных чисел из списка
random_sample = random.sample(numbers, 3)
print(f"Три случайных числа из списка: {random_sample}")