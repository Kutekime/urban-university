import unittest
import logging

# Настройка уровня логирования
logging.basicConfig(level=logging.DEBUG)

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance: # ошибка в том, что если два бегуна пересекут линию
                    # в одну итерацию, то будет первым не тот, кто фактически быстрее пробежал, а тот, кто был раньше
                    # обработан. Решается, например, так - ранжируем финишёров в зависимости от расстояния,
                    # которое они пробежали
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

def frozen_test(method):
    def wrapper(self):
        if self.is_frozen:
            logging.debug(f'Тесты в кейсе {self.__str__()} заморожены (skipped)!\nВерить сообщению выше')
            return
        method(self)

    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls): #метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться
        # результаты всех тестов.
        cls.all_results = {}
        cls.is_frozen = True

    def setUp(self): #метод, где создаются 3 объекта:
        self.r_Usain = Runner('Усэйн', 10)
        self.r_Andrey = Runner('Андрей', 9)
        self.r_Nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls): #метод, где выводятся all_results по очереди в столбец.
        for _tournament_number in cls.all_results:
            print(cls.all_results[_tournament_number])

    # Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
    # У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
    # В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
    # (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
    @unittest.skipIf(is_frozen, 'Тест заморожен!')
    def test_run1(self):
        self.tournament = Tournament(90, self.r_Nick, self.r_Usain)  #Расположил "r_Nick"
        # в начале, чтобы было очевидно, что распределение мест происходит верно
        self.all_results.update({1 : self.tournament.start()})
        self.assertTrue(self.all_results[1][2] == 'Ник')

    @frozen_test #Реализовал сначала свой декоратор (в лекции опущено слово декоратор, что сбило меня с толку),
    # который выводит сообщение прямо в лог, при запуске теста!
    def test_run2(self):
        self.tournament = Tournament(90, self.r_Nick, self.r_Andrey)
        self.all_results.update({2 : self.tournament.start()})
        self.assertTrue(self.all_results[2][2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тест заморожен!')
    def test_run3(self):
        self.tournament = Tournament(90, self.r_Nick, self.r_Usain, self.r_Andrey)
        self.all_results.update({3 : self.tournament.start()})
        self.assertTrue(self.all_results[3][3] == 'Ник')

if __name__ == '__main__':
    unittest.main()