# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

args = ['сетевое программирование', 'сокет', 'декоратор']

# Создаю текстовый файл test_file.txt, заполняю его тремя строками
with open('test_file.txt', 'w') as file_name:
    for i in args:
        file_name.write(i + '\n')
    file_name.seek(0)

# проверяю кодировку файла по умолчанию
print(file_name)

codin_file = locale.getpreferredencoding()

# Принудительно открываю файл в формате Unicode и вывести его содержимое.
with open('test_file.txt', 'r', encoding=codin_file) as file_name:
    for i in file_name:
        print(i)

    file_name.seek(0)


