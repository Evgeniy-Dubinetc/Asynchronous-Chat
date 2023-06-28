"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet
import os

ARGS = ['ping', 'yandex.ru']
YANDEX_URL = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(YANDEX_URL.stdout)
for line in YANDEX_URL.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))
print(os.name)


ARGS = ['ping', 'youtube.com']
YOUTUBE_URL = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(YOUTUBE_URL.stdout)
for line in YOUTUBE_URL.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']), end='')
print(os.name)