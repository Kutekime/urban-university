class Animal:
    alive = True
    fed = False

    def __init__(self, name):
         self.name = name

class Plant:
    edible = False

    def __init__(self, name):
         self.name = name

class Eating(Animal):
    def eat(self, food):
        if not food.edible:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True

class Mammal(Eating):
    pass

class Predator(Eating):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)