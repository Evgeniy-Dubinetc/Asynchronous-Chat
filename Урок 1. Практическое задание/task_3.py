"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


# my_list = [b'attribute', b'класс', b'функция', b'type']
# строки на кириллице выдают синтаксическую ошибку, try: except: ошибку не ловит
'''File "/home/ed/Рабочий стол/Assinc_chat/Урок 1. Практическое задание/task_3.py", line 12
    my_list = [b'attribute', b'класс', b'функция', b'type']
                            ^
SyntaxError: bytes can only contain ASCII literal characters.'''


new_list = []

try:
    my_list = ['attribute', 'класс', 'функция', 'type']
    for i in my_list:
        new_list.append("b'{}'".format(i))
except SyntaxError:
    print('bytes can only contain ASCII literal characters')
print('типа байтовые строки без ошибки :)    {}'.format(new_list))
