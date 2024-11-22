import inspect
import sys
from pprint import pprint

def introspection_info(obj):
  print('Вы работаете на следующей платформе:', sys.platform)
  info = {'Тип' : type(obj), 'Атрибуты и методы объекта' : dir(obj),
          'Модуль (класс), к которому объект принадлежит' : inspect.getmodule(obj)}
  if type(obj) == int:
    print(f'Вы передали число!\nЧисло {obj} занимает {obj.bit_length()} бит\n')
  pprint(info)
  '''
  Для себя отмечу, ещё есть:
  help()
  hasattr(), getattr(some_object, attribute_1)
  callable()
  
  «Builtins» — это псевдомодуль, который включает в себя встроенные в интерпретатор объекты. Это значит,
  что в нём содержатся такие элементы, как константы, исключения и функции, доступные в любой программе на Python
  без необходимости их явного импорта.
  
  Вставив содержимое модуля «builtins» (__builtins__)в функцию 'dir',
  мы можем получить полный список всех встроенных функций и переменных, доступных в Python (если выполнить снаружи)
  
  sys.setrecursionlimit() и другие лимиты..
  sys.getsizeof()
  '''


number_info = introspection_info(42)

