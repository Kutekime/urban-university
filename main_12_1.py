import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    Jho = Runner('Jho')
    Bill = Runner('Bill')

    def reset(self, *runner):
        for r in runner:
            r.distance = 0

    def test_walk(self): #метод, в котором создаётся объект класса Runner с произвольным именем.
        # Далее
        # вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
        self.reset(self.Jho) #Понял, что reset здесь есть встроенный, но уже не стал переделывать
        for _ in range(10):
            self.Jho.walk()
        self.assertEqual(self.Jho.distance, 50)

    def test_run(self): #метод, в котором создаётся объект класса Runner с произвольным именем. Далее
        # вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
        self.reset(self.Bill)
        for _ in range(10):
            self.Bill.run()
        self.assertEqual(self.Bill.distance, 100)

    def test_challenge(self): #метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у
        # объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными,
        # используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        '''
        Понял, что запускать метод теста внутри друго теста - плохая идея, так как первый тест может
        "перекрыть" собой тест в котором он запущен. Хотя, в обычном коде - это must-have
        :return:
        '''
        
        for _ in range(10):
            self.Jho.walk()
        
        for _ in range(10):
            self.Bill.run()
        self.assertNotEqual(self.Jho.distance, self.Bill.distance, 'Джо опять считерил!')
        self.reset(self.Jho, self.Bill)



if __name__ == '__main__':
    unittest.main()
