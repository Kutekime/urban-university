# print('Hi, PyCharm')
# x = 43
# y = 32
# print(x * y)
# print("End line")

# first = input('Введите первое число: ')
# second = input('Введите второе число: ')
# third = input('Введите третье число: ')
# if first == second and first == third:
#     print(3)
# elif first == second or first == third or second == third:
#     print(2)
# else:
#     print(0)

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[i] >= 0:
    if my_list[i] == 0:
        i += 1
        continue
    elif i + 1 == len(my_list):
        break
    else:
        print (my_list[i])
        i += 1
