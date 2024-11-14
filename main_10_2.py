import threading
#import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.counter = 0
        self.timer_event = threading.Event()

    def start_timer(self):
        # запускаем таймер на 1 секунду
        self.timer_event.clear() #не сразу нашёл это решение, чтобы таймер срабатывал каждый раз в цикле
        threading.Timer(1, self.timer_event.set).start() #Когда таймер срабатывает,
        # он вызывает метод self.timer_event.set(), устанавливая событие в активное состояние.

    def run(self):
        print(f'{self.name}, на вас напали!')
        #100 врагов-потоков
        while self.enemy != 0:
            # рыцаря.
            #time.sleep(1) заморочился и сделал реализацию через threading.Timer
            self.start_timer()
            self.timer_event.wait() #вызывается метод self.timer_event.wait(), который блокирует выполнение программы
            # до тех пор, пока событие не станет активным (то есть пока таймер не сработает).
            self.enemy = self.enemy - self.power  # В процессе сражения количество врагов уменьшается на power текущего
            self.counter += 1
            print(f'{self.name}, сражается {self.counter} дней(я)..., осталось {self.enemy} врагов(а).')
        print(f'{self.name}, одержал победу спустя {self.counter} дней(дня)!\n')

# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Сир, все враги были повержены! Особо отличились рыцари {first_knight.name} и {second_knight.name}!')
