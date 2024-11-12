# def apply_all_func(int_list, *functions):
#     #int_list список из чисел (int, float)
#     results = {}
#     for fun in functions: #неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
#         res = fun(int_list)
#         results.update({fun.__name__ : res})
#     return results
#
#
#
#     # !min - принимает список, возвращает минимальное значение из него.
#     # !max - принимает список, возвращает максимальное значение из него.
#     # !len - принимает список, возвращает кол-во элементов в нём.
#     # !sum - принимает список, возвращает сумму его элементов.
#     # !sorted - принимает список, возвращает новый отсортированный список на основе переданного.
#
#
# print(apply_all_func([6, 20, 15, 9], max, min))
# print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
# second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#
# first_result = [x.__len__() for x in first_strings if x.__len__() > 4]
# second_result = [(x, y) for x in first_strings for y in second_strings if x.__len__() == y.__len__() ]
# third_result = {x : x.__len__() for x in first_strings + second_strings if not x.__len__() % 2}
#
# print(first_result)
# print(second_result)
# print(third_result)

# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']
# first_result = (x[0].__len__() - x[1].__len__() for x in zip(first, second) if not x[0].__len__() == x[1].__len__())
# second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
#
# #     В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк
# # в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
# #!!! Я офигеваю от такой резкой смены парадигмы, которую мы не проходили
#
# print(list(first_result))
# print(list(second_result))


# from random import choice
#
# #Lambda-функция:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# print(list(map(lambda x, y: x == y, first, second)))
#
# #Замыкание:
# # Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# # Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
# # неограниченное количество данных любого типа.
# # Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# # Функция get_advanced_writer возвращает функцию write_everything.
# def get_advanced_writer(file_name):
#     def write_everything(*data_set):
#         with  open(file_name, 'w', encoding='utf-8') as file:
#             for data in data_set:
#                 file.write(str(data) + '\n')
#     return write_everything
#
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#
# #Метод __call__:
# class MysticBall:
#     def __init__(self, *words):
#         self.words = words
#
#     def __call__(self):
#         return choice(self.words)
#
#
# first_ball = MysticBall('Да', 'Нет', 'Наверное')
# print(first_ball())
# print(first_ball())
# print(first_ball())
#
# # Примерный результат (может отличаться из-за случайности выбора):
# # Да
# # Да
# # Наверное
#
# # У меня круче получилось :P :
# # Да
# # Наверное
# # Нет

# class StepValueError(ValueError):
#     pass
#
# class Iterator:
#     def __init__(self, start, stop, step = 1):
#         self.start = start #целое число, с которого начинается итерация.
#         self.stop = stop #целое число, на котором заканчивается итерация.
#         self.inf_err = False
#         if step == 0:
#             print('Ошибка! Шаг не может быть равен 0\n'
#                   'Для корректной работы увеличиваю шаг на 1')
#             self.step = step + 1
#         else:
#             self.step = step #шаг, с которым совершается итерация.
#         if (start > stop and self.step > 0) or (start < stop and self.step < 0):
#             self.inf_err = True
#             self.step = self.step * -1
#         self.pointer = start #указывает на текущее число в итерации (изначально start)
#
#     def __iter__(self): #метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
#         if self.inf_err:
#             print('Обнаружен бесконечный итератор! Для исправления ситуации инвертирую шаг!')
#         self.pointer = self.start
#         return self
#
#     def __next__(self): #метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация
#         # завершится либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
#         if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
#             raise StopIteration()
#         result = self.pointer
#         self.pointer += self.step  # не понял, почему по разному считает, если например эту строчку сделать выше условия
#         return result
#
# # try:
# #
# # except StepValueError:
# #     print('Шаг указан неверно') сейчас не нужно, видимо задачу пределали, а это забыли убрать..
# iter1 = Iterator(100, -200, 0)
# for i in iter1:
#     print(i, end=' ')
# print()
#
# '''
#     Получается не очень красиво, т.к. выскакиевает Traceback, но зато с нашим пояснением:
#     __main__.StepValueError: шаг не может быть равен 0
#
#     ***
#     Потом я понял, зачем обернули в try except: дальше код не выполняется, поэтому заменил raise на if...
#
#     Затем учёл даже случай, когда шаг был 0, я его увеличил на 1 и получился бесконечный цикл.
#     Чтобы проверка сработала, проверяю не step, а self.step
# '''
#
# iter2 = Iterator(-5, 1)
# iter3 = Iterator(6, 15, 2)
# iter4 = Iterator(5, 1, -1)
# iter5 = Iterator(10, 1)
#
#
# for i in iter2:
#     print(i, end=' ')
# print() #сначала этот print тоже сделал с отступом...
# for i in iter3:
#     print(i, end=' ')
# print()
# for i in iter4:
#     print(i, end=' ')
# print()
# for i in iter5:
#     print(i, end=' ')
# print()

# def all_variants_beta(text): #которая принимает строку text и возвращает объект-генератор,
#     # при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#     i = 0
#     l = text.__len__()
#     while i != l:
#         yield text
#         i += 1
#
# def all_variants(text):
#     l = text.__len__()
#     for length in range(1, l + 1):  # Длина подстроки от 1 до полной длины строки
#         for start in range(l - length + 1):  # Стартовый индекс для текущей длины
#             yield text[start:start + length]
#
# a = all_variants("abc")
# for i in a:
#     print(i)
# # Вывод на консоль:
# # a
# # b
# # c
# # ab
# # bc
# # abc



def is_prime(func):
    def wrapper(*args):
        __result = func(*args)
        is_pr = 'Простое'
        if __result < 2:
            pass
        else:
            for i in range(2, int(__result ** 0.5) + 1):
                if __result % i == 0:
                    is_pr = 'Составное'
        print(is_pr)
        return __result
    return wrapper

@is_prime
def sum_three(a, b ,c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)