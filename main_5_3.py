class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return  self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print('Внимание, вы патаетесь сделать операцию не с объектом класса "House"!')

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for y in [x + 1 for x in range(new_floor)]:
                print(y)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__