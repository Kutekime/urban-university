from main_12_1 import RunnerTest
from main_12_2 import TournamentTest

import unittest


# Создание объекта TestSuite
runners = unittest.TestSuite()

# Добавление тестовых случаев
#runners.addTest(test_calc.makeSuite(...)) устаревший способ
runners.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runners.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Запуск тестов
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runners)

