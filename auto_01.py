from random import random

time = 5
car_positions = [1, 1, 1]

# Функция для уменьшения времени на 1
def decrease_time(time):
    time -= 1
    return time

# Функция для перемещения машин с вероятностью 70%
def move_cars(car_positions):
    for i in range(len(car_positions)):
        if random() > 0.3:
            car_positions[i] += 1

# Функция для отрисовки позиций машин
def draw_cars(car_positions):
    for pos in car_positions:
        print('-' * pos)
    print('')  # Печатаем пустую строку между итерациями

while time > 0:
    time = decrease_time(time)
    move_cars(car_positions)
    draw_cars(car_positions)



