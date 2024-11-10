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

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (x[0].__len__() - x[1].__len__() for x in zip(first, second) if not x[0].__len__() == x[1].__len__())
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

#     В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк
# в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
#!!! Я офигеваю от такой резкой смены парадигмы, которую мы не проходили

print(list(first_result))
print(list(second_result))
