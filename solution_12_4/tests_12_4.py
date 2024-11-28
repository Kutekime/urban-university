import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    Jho = Runner('Jho')
    Bill = Runner('Bill')
    is_frozen = False

    def reset(self, runner):
        runner.distance = 0


    @unittest.skipIf(is_frozen, 'Тест заморожен!')
    def test_walk(self): #метод, в котором создаётся объект класса Runner с произвольным именем.
        # Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
        try:
            self.Jho_negative = Runner('Jho', speed=-5)
            self.reset(self.Jho_negative)
            for _ in range(10):
                self.Jho_negative.walk()
            self.assertEqual(self.Jho_negative.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner (test_walk)\n { e }") #заметил, что важно передавать через
            # f-строку (или форматирование через %), если написать, через запятую, то ошибка "запускается", выводится в
            # консоль и логгирование не работает

    @unittest.skipIf(is_frozen, 'Тест заморожен!')
    def test_run(self): #метод, в котором создаётся объект класса Runner с произвольным именем. Далее
        # вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
        try:
            self.Bill_wrong = Runner(5)
            self.reset(self.Bill_wrong)
            for _ in range(10):
                self.Bill_wrong.run()
            self.assertEqual(self.Bill_wrong.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner (test_run)\n { e }")

    @unittest.skipIf(is_frozen, 'Тест заморожен!')
    def test_challenge(self): #метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у
        # объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными,
        # используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        '''
        Понял, что запускать метод теста внутри друго теста - плохая идея, так как первый тест может
        "перекрыть" собой тест в котором он запущен. Хотя, в обычном коде - это must-have
        :return:
        '''
        self.reset(self.Jho)
        for _ in range(10):
            self.Jho.walk()
        self.reset(self.Bill)
        for _ in range(10):
            self.Bill.run()
        self.assertNotEqual(self.Jho.distance, self.Bill.distance, 'Джо опять считерил!')

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")


if __name__ == '__main__':
    unittest.main()