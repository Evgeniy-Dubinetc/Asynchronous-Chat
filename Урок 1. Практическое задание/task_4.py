"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
for i in my_list:
    b_str = i.encode('utf-8')
    print(b_str, type(b_str))
    re_str = bytes.decode(b_str, 'utf-8')
    print(re_str, type(re_str), '\n')

