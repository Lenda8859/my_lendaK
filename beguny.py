from random import random

time = 10
runner = [1, 1, 1]

# Создаем пустой список
winner1 = []
winner2 = []
winner3 = []

sum_win1 = sum(winner1)
sum_win2 = sum(winner2)

def min_time(time):
    time -= 1
    return time

def move_run (runner):
    for i in range (len(runner)):
        if random() > 0.5:
            runner[i] += 1
            winner1.append(i)
        elif
            if random() < 0.5:
            runner[i] += 1
            winner2.append(i)
        else:
            winner3.append(i)

def draw_run(runner):
    for pos_r in runner:
        print('*' * pos_r)

def winner_run():
    if sum_win1 > sum_win2:
        print("Победил бегун: ", winner1)
    else:
        print("победил бегун: ", winner2)


while time > 0:
    time = min_time(time)
    move_run(runner)
    draw_run(runner)
    print('')


print(winner_run)
