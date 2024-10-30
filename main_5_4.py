class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        #cls.__instance = super().__new__(cls) для создания уникальных объектов (ссылка на него записывается в
        # __instance)
        #return cls.__instance при последующих вызовах будем возращать этот же __instance
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return  self.number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

