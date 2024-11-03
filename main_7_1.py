from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    def get_products(self): #который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
        #строку со всеми товарами из файла __file_name.
        file = open(self.__file_name, 'r')
        ret = file.read()
        #pprint(file.read())
        file.close()
        return ret

    def add(self, *products): #Принимает неограниченное количество объектов класса Product. Добавляет в файл
        #__file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть,
        # то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.

        for x in products:
            get_products = self.get_products() #для корректной работы, данные нужно считывать на каждом шаге
            if get_products.find(str(x.name)) == -1: #заметил, что при поиске оперирует целыми строками
                file2 = open(self.__file_name, 'a') #упорно пытался сначала снова использовать переменную file ><
                file2.write(str(x) + '\n')
                file2.close()
            else:
                print(f'Продукт {x.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())