"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

b_list = [b'class', b'function', b'method']

for b in b_list:
    print('тип: {}'.format(type(b)))
    print('содержимое: {}'.format(b))
    print('длина {} символов \n'.format(len(b)))
