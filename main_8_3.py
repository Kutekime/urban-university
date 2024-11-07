class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model #название автомобиля (строка).
        self.__vin = __vin #vin номер автомобиля (целое число). Уровень доступа private.
        self.__numbers = __numbers #номера автомобиля (строка).
        self.__is_valid_vin() #пишут так правильней, чем __is_valid_vin(self)
        self.__is_valid_numbers()

    def __is_valid_vin(self): #принимает vin_number и проверяет его на корректность. Возвращает (True),
        # если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
        if not isinstance(self.__vin, int) or self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber('Неверно указан вин-номер! Проверьте, что это целое число из 6-ти цифр')
        else:
            return True

    def __is_valid_numbers(self): #принимает numbers и проверяет его на корректность. Возвращает (True, если)
        # корректный, в других случаях выбрасывает исключение. Уровень доступа private.
        if not isinstance(self.__numbers, str) or not self.__numbers.__len__() == 6:
            raise IncorrectCarNumbers('Неверно указан номер! Проверьте, что это текст равный 6-ти символам')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

#Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение,
# которое будет выводиться при выбрасывании исключения.

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
