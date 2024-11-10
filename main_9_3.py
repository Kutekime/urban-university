first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (x[0].__len__() - x[1].__len__() for x in zip(first, second) if not x[0].__len__() == x[1].__len__())
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

#     В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк
# в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
#!!! Я офигеваю от такой резкой смены парадигмы, которую мы не проходили

print(list(first_result))
print(list(second_result))
