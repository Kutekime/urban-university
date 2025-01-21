import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_email ON users (email)') #создал уникальный индекс, чтобы можно
# было ниже написать INSERT OR IGNORE

# for i in range(1, 11):
#     cursor.execute('INSERT OR IGNORE INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}',
#                                                                                            f'ex{i}@gmail.com',
#                                                                                            str(i * 10),
#                                                                                            '1000'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users set balance = ? WHERE username = ?', ('500', f'User{i}'))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))


# cursor.execute(("SELECT CONCAT('Имя: ', username, ' | Почта: ', email, ' | Возраст: ', age, ' | Баланс: ', "
#                 "balance) AS user_info FROM Users WHERE not age = ?"), (60,))

''' ВТОРОЕ ЗАДАНИЕ: '''

cursor.execute('DELETE FROM Users WHERE id = ?', ('6',))
cursor.execute('SELECT COUNT(*) FROM Users')
result1 = cursor.fetchone()[0]
print(result1)
cursor.execute('SELECT SUM(balance) FROM Users')
result2 = cursor.fetchone()[0]
print(result2)
cursor.execute('SELECT AVG(balance) FROM Users')
result3 = cursor.fetchone()[0]
print(int(result3))
print(int(result2 / result1)) #как вариант, когда нужно избегать делать дополнительные запросы

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()