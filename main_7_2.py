def custom_write(file_name, strings): #которая принимает аргументы file_name - название файла для (записи,
    #strings - список) строк для записи.
    file = open(file_name, 'w', encoding='utf-8')
    dic = {}
    for i, x in enumerate(strings):
        dic.update({(i, file.tell()): x})
        file.write(x + '\n')
    file.close()
    return dic

    # Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    # а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)