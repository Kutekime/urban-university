def personal_sum(numbers):
    incorrect_data = 0
    total = 0
    count = 0
    try:
        for num in numbers:
            total += num
            count += 1
    except TypeError as exc:
        print(f'Некорректный тип данных для подсчёта суммы - {exc.args}')
        incorrect_data += 1
    return (total, count, incorrect_data)

def calculate_average(numbers):
    try:
        numbers.__iter__()
        return personal_sum(numbers)[0] / personal_sum(numbers)[1]
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
    except AttributeError:
        print('Поймал новую ошибку - AttributeError\n А через TypeError в функции "calculate_average" ошибка не '
              'ловится, так как перебор, например, тут не происходит')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать