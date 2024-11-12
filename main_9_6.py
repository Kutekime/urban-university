def all_variants_beta(text): #которая принимает строку text и возвращает объект-генератор,
    # при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
    i = 0
    l = text.__len__()
    while i != l:
        yield text
        i += 1

def all_variants(text):
    l = text.__len__()
    for length in range(1, l + 1):  # Длина подстроки от 1 до полной длины строки
        for start in range(l - length + 1):  # Стартовый индекс для текущей длины
            yield text[start:start + length]

a = all_variants("abc")
for i in a:
    print(i)
