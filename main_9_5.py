class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start = start #целое число, с которого начинается итерация.
        self.stop = stop #целое число, на котором заканчивается итерация.
        self.inf_err = False
        if step == 0:
            print('Ошибка! Шаг не может быть равен 0\n'
                  'Для корректной работы увеличиваю шаг на 1')
            self.step = step + 1
        else:
            self.step = step #шаг, с которым совершается итерация.
        if (start > stop and self.step > 0) or (start < stop and self.step < 0):
            self.inf_err = True
            self.step = self.step * -1
        self.pointer = start #указывает на текущее число в итерации (изначально start)

    def __iter__(self): #метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
        if self.inf_err:
            print('Обнаружен бесконечный итератор! Для исправления ситуации инвертирую шаг!')
        self.pointer = self.start
        return self

    def __next__(self): #метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация
        # завершится либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        result = self.pointer
        self.pointer += self.step  # не понял, почему по разному считает, если например эту строчку сделать выше условия
        return result

# try:
#
# except StepValueError:
#     print('Шаг указан неверно') сейчас не нужно, видимо задачу пределали, а это забыли убрать..
iter1 = Iterator(100, -200, 0)
for i in iter1:
    print(i, end=' ')
print()

'''
    Получается не очень красиво, т.к. выскакиевает Traceback, но зато с нашим пояснением:
    __main__.StepValueError: шаг не может быть равен 0

    ***
    Потом я понял, зачем обернули в try except: дальше код не выполняется, поэтому заменил raise на if...
    
    Затем учёл даже случай, когда шаг был 0, мы его увеличили на 1 и получился бесконечный цикл.
    Чтобы проверка сработала, проверяю не step, а self.step
'''

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print() #сначала этот print тоже сделал с отступом...
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
