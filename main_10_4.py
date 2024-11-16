import threading
import time
from queue import Queue
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

#thread_g = [0, 1, 2, 3, 4, 5]
class Cafe:
    def __init__(self, *tables):
        self.Tables = ()
        for table in tables:
            self.Tables += (table,)
        #print(self.Tables[2].quest)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            guest_seating = False
            for table in self.Tables:
                if table.guest is None:
                    table.guest = guest
                    #thread_g[table.number] = threading.Thread(target=guest)
                    #thread_g[table.number].start() Да, тут я напутал сначала (эта заметка больше для себя)
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest_seating = True
                    break
            if guest_seating:
                continue
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self): # Этот метод имитирует процесс обслуживания гостей.
        while not self.queue.empty():
            for table in self.Tables:
                if not (table.guest is None or table.guest.is_alive()):
                    print(f'{table.guest.name} поел(-а) и ушёл(ушла)\n Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        queue_guest = self.queue.get()
                        table.guest = queue_guest
                        print(f'{queue_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        queue_guest.run()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
