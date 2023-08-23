# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. 
# В файле должен храниться список словарей, словарь описывает элемент внутри директории: имя, расширение, тип. 
# Если элемент - директория, то только тип и имя. 
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }

import os
import json

def serialize_directory():
    files = []
    for item in os.listdir('.'):
        if os.path.isfile(item):
            name = os.path.splitext(item)[0]
            extension = os.path.splitext(item)[1]
            file = {
                'name': name,
                'extension': extension,
                'type': 'file'
            }
            files.append(file)
        elif os.path.isdir(item):
            dir = {
                'name': item,
                'type': 'directory'
            }
            files.append(dir)

    with open('directory.json', 'w') as json_file:
        json.dump(files, json_file, indent=4)

serialize_directory()