import requests

r = requests.get('https://api.github.com/events')

print(r.status_code) #если 200, значит всё ок
print(r.encoding) #вернёт нам знакомую кодировку "utf-8" в этом примере
#print(r.text) # Получить текст в виде элементов списка, который был автоматически декодирован с сервера
#print(r.json()) # Получить JSON с помощью встроченного JSON декодера
print('Ава:', r.json()[0]['actor']['avatar_url']) # Вывели конкретный элемент из JSON, а именно ссылку на аватарку

print('\nResponse Headers (заголовки, которые мы получаем с сервера):')
for info in r.headers:
    print(info + ': ', r.headers[info])