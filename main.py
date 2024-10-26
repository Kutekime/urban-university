# def divide(first , second):
#     if second != 0:
#         return first / second
#     else:
#         return 'Ошибка'
#
# from math import inf
#
# def divide(first , second):
#     if second != 0:
#         return first / second
#     else:
#         return inf

from fake_math import divide as f_d
from true_math import divide as t_d

result1 = f_d(69, 3)
result2 = f_d(3, 0)
result3 = t_d(49, 7)
result4 = t_d(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)