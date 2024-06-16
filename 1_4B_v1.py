import pandas as pd

def process_data(input_file, output_file):
    # Загрузка данных из CSV файла
    df = pd.read_csv(input_file)

    # Создание нового столбца 'Total'
    df['Total'] = df['Quantity'] * df['Price'] + df['Freight']

    # Отображение выборочных столбцов (например, первые 10 строк и интересующие столбцы)
    print(df.head(10)[['Quantity', 'Price', 'Freight', 'Total']])

    # Сохранение всех данных в новый CSV файл
    df.to_csv(output_file, index=False)

# Указываем пути к файлам
input_file = r'D:\Моя папка\N\ITMO\Python_Базовые возможности\Практика_задания\data\orderdata_sample.csv'
output_file = r'D:\Моя папка\N\ITMO\Python_Базовые возможности\Практика_задания\data\orderdata_processed.csv'

# Вызываем функцию для обработки данных
process_data(input_file, output_file)
