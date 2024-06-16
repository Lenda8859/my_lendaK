import datetime
current_date = datetime.date.today()
year = current_date.year
#Задание 1. Проверка с условиями if-else
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Год высокосный")
        else:
            print("Год не высокосный")
    else:
        print("Год высокосный")
else:
    print("Год не высокосный")
#Задание 2. Проверка с дополнительными условиями elif
if year % 400 == 0:
    print("Год высокосный")
elif year % 100 == 0:
    print("Год не высокосный")
elif year % 4 == 0:
    print("Год высокосный")
else:
    print("Год не высокосный")
#Задание 3. Проверка с помощью логических операторов в одну строку if
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Год высокосный")
else:
    print("Год не высокосный")
#Задание 4. Проверка с применением специальной функции модуля calendar
import calendar
if calendar.isleap(year):
    print("Год высокосный")
else:
    print("Год не высокосный")
print("Теукщая дата:", current_date)