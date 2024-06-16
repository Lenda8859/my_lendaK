import os

# Создаем директорию для файлов, если она не существует
folder = r'D:\Моя папка\N\ITMO\ДЗ\PythonPrim\Textfiles'
if not os.path.exists(folder):
    os.makedirs(folder)

# Создаем и записываем содержимое в файлы file1.txt, file2.txt, file3.txt
file_contents = {
    'file1.txt': 'Hello, this is the first file.\nIt contains some sample text.',
    'file2.txt': 'This is the second file.\nIt also has some text.',
    'file3.txt': 'And this is the third file.\nIt has different content.',
}
for filename, content in file_contents.items():
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Создание файлов в {folder} завершено")

# Поиск файлов, содержащих заданную подстроку
answ = set()
search = input("Введите поисковый запрос: ")
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as fp:
            for line in fp:
                if search in line:
                    answ.add(filename)
                    break

# Выводим найденные файлы
for i in answ:
    print(i)

# Создаем файл file4.tx. и записывам в него содержимое
file_contents1 = {
    'file4.txt': '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.'''
}
for filename1, content in file_contents1.items():
    filepath1 = os.path.join(folder, filename1)
    with open(filepath1, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Создание файла в {folder} завершено")

#Функция для получения статистики о файле
def file_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        letters_count = sum(map(str.isalpha, content))
        words_count = len(content.split())
        lines_count = content.count('\n') + 1
        print("Input file contains:")
        print(f"{letters_count} letters")
        print(f"{words_count} words")
        print(f"{lines_count} lines")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

file_path = os.path.join(folder, 'file4.txt')
file_statistics(file_path)

from pathlib import Path

home = Path.home()
my_folder = home / "my_folder"

if not my_folder.exists():
    my_folder.mkdir()

file1 = my_folder / "file1.txt"
file1.write_text("Hello, this is file.txt")

(file1.parent / "file2.txt"). write_text("Hello, this is file2.txt")

image_file = my_folder / "image.png"
image_file.touch()

images_folder = my_folder / "images"
images_folder.mkdir(exist_ok=True)

image_file.replace(images_folder / image_file)

print("Директория и файлы созданы и перемещены успешно")

import shutil
from pathlib import Path

home = Path.home()
source_folder = home / "my_folder"

target_folder = r'D:\Моя папка\N\ITMO\ДЗ\PythonPrim'

try:
    shutil.move(str(source_folder), target_folder)
    print(f"Lbhtrnjhbz {source_folder} успешно перемещена в {target_folder}.")

except Exception as e:
    print(f"Ошибка при перемешении директории: {e}")

from pathlib import Path
import shutil
import sys

# Проверяем, что в командной строке передан ровно один аргумент (имя каталога)
if len(sys.argv) != 2:
    print("Использование: python имя_программы.py Имя_каталога")
    sys.exit(1)

# Имя каталога, в который будем перемещать файлы
target_dir_name = sys.argv[1]

# Путь к текущему рабочему каталогу
current_dir = Path.cwd()

# Полный путь к целевому каталогу, который создаем/перемещаем
target_dir = current_dir / target_dir_name

try:
    # Создаем целевой каталог, если он не существует
    target_dir.mkdir(exist_ok=True)

    # Перемещаем все текстовые файлы из текущего каталога в целевой каталог
    for file in current_dir.glob('*.txt'):
        shutil.move(str(file), str(target_dir / file.name))

    print(f"Все текстовые файлы были перемещены в каталог {target_dir}.")
except Exception as e:
    print(f"Ошибка при перемещении файлов: {e}")
