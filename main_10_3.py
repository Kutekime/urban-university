from random import randint
import time
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        rand = 0
        __count = 0

        for i in range(0, 100):
            rand = randint(50, 500)
            self.balance += rand
            __count = self.balance
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение на: {__count} денег. Баланс: {self.balance}')
            time.sleep(0.001)
        print(f'За 100 транзакций удалось пополнить на: {__count} денег. Баланс на конец пополнений: {self.balance}')


    def take(self):
        rand = 0
        __count = 0

        for i in range(0, 100):
            print(f'Запрос на снятие: {rand} денег.')
            rand = randint(50, 500)

            if self.balance >= rand:
                self.balance -= rand
                __count += rand
                print(f'Снятие: {rand} денег. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print(f'Запрос отклонён: недостаточно средств')
            time.sleep(0.001)
        print(f'За 100 транзакция удалось снять: {__count} денег. Баланс на конец снятий: {self.balance}')

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,)) #здесь args=(bk,) передает кортеж, содержащий одну ссылку на
# объект bk, что является правильным синтаксисом для передачи аргументов в функцию через threading.Thread.

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
