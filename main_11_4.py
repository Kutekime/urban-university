# import requests
#
# r = requests.get('https://api.github.com/events')
#
# print(r.status_code) #если 200, значит всё ок
# print(r.encoding) #вернёт нам знакомую кодировку "utf-8" в этом примере
# #print(r.text) # Получить текст в виде элементов списка, который был автоматически декодирован с сервера
# #print(r.json()) # Получить JSON с помощью встроченного JSON декодера
# print('Ава:', r.json()[0]['actor']['avatar_url']) # Вывели конкретный элемент из JSON, а именно ссылку на аватарку
#
# print('\nResponse Headers (заголовки, которые мы получаем с сервера):')
# for info in r.headers:
#     print(info + ': ', r.headers[info])


# pip install -r requirements.txt
# pip freeze
# python -m venv venv
# .\venv\Scripts\activate
# python main.py

# import numpy as np
# import pygame as pg
#
#
# fps = pg.time.Clock()
# screen = pg.display.set_mode((510, 510))
# map_colors = np.arange(0, 510)
# for i in map_colors:
#     for j in map_colors:
#         surf = pg.Surface((1, 1))
#         surf.fill((i // 2, i // 2, i // 2))
#         screen.blit(surf, (i, j))
#
# r = 0
# g = 0
# b = 255
# circle_start_size = 1
# circle_end_size = 50
# current_size = circle_end_size
# size_dir = 1
#
# while True:
#
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             exit()
#     if pg.mouse.get_pressed()[0]:
#         pg.draw.circle(screen, (r, g, b), pg.mouse.get_pos(), current_size, 2)
#
#     if r < 255 and g == 0:
#         r += 1
#         b -= 1
#     elif g < 255 and b == 0:
#         g += 1
#         r -= 1
#     else:
#         b += 1
#         g -= 1
#
#     if current_size in (circle_start_size, circle_end_size):
#         size_dir *= -1
#
#     current_size += size_dir
#
#     fps.tick(60)
#     pg.display.update()

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

