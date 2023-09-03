import sqlite3

from typing import Any


def print_results(result_list: list[Any]) -> None:
    print('Выводим результаты\n')

    result: Any
    for result in result_list:
        print(result)
    print('')


# Устанавливаем соединение с базой данных
print('Устанавливаем соединение с базой данных\n')

connection: sqlite3.Connection = sqlite3.connect('my_database.db')
cursor: sqlite3.Cursor = connection.cursor()

# Создаем таблицу Users
print('Создаем таблицу Users\n')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,    
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Создаем индекс для столбца "email"
print('Создаем индекс для столбца "email"\n')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Добавляем новых пользователей
print('Добавляем новых пользователей\n')

cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser2', 'newuser2@example.com', 25))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser3', 'newuser3@example.com', 50))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser4', 'newuser4@example.com', 25))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser5', 'newuser5@example.com', 35))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser6', 'newuser6@example.com', 50))
cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('newuser7', 'newuser7@example.com'))

# Обновляем возраст пользователя "newuser"
print('Обновляем возраст пользователя "newuser"\n')

cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

# Удаляем пользователя "newuser"
print('Удаляем пользователя "newuser"\n')

cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# Выбираем всех пользователей
print('Выбираем всех пользователей\n')

cursor.execute('SELECT * FROM Users')
users: list[Any] = cursor.fetchall()

# Выводим результаты
print_results(users)

# Выбираем имена и возраст пользователей старше 25 лет
print('Выбираем имена и возраст пользователей старше 25 лет\n')

cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results: list[Any] = cursor.fetchall()

print_results(results)

# Получаем средний возраст пользователей для каждого возраста
print('Получаем средний возраст пользователей для каждого возраста\n')

cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results: list[Any] = cursor.fetchall()

print_results(results)

# Фильтруем группы по среднему возрасту больше 30
print('Фильтруем группы по среднему возрасту больше 30\n')

cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filtered_results: list[Any] = cursor.fetchall()

print_results(filtered_results)

# Выбираем и сортируем пользователей по возрасту по убыванию
print('Выбираем и сортируем пользователей по возрасту по убыванию\n')

cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
results: list[Any] = cursor.fetchall()

print_results(results)

# Выбираем и сортируем пользователей по возрасту по убыванию
print('Выбираем и сортируем пользователей по возрасту по убыванию\n')

cursor.execute('''
SELECT username, age, AVG(age)
FROM Users
GROUP BY age
HAVING AVG(age) > ?
ORDER BY age DESC
''', (30,))
results = cursor.fetchall()

print_results(results)

# Подсчет общего числа пользователей
print('Подсчет общего числа пользователей\n')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users: Any = cursor.fetchone()[0]

print('Общее количество пользователей: ' + str(total_users) + '\n')

# Вычисление суммы возрастов пользователей
print('Вычисление суммы возрастов пользователей\n')

cursor.execute('SELECT SUM(age) FROM Users')
total_age: Any = cursor.fetchone()[0]

print('Общая сумма возрастов пользователей: ' + str(total_age) + '\n')

# Вычисление среднего возраста пользователей
print('Вычисление среднего возраста пользователей\n')

cursor.execute('SELECT AVG(age) FROM Users')
average_age: Any = cursor.fetchone()[0]

print('Средний возраст пользователей: ' + str(average_age) + '\n')

# Нахождение минимального возраста
print('Нахождение минимального возраста\n')

cursor.execute('SELECT MIN(age) FROM Users')
min_age: Any = cursor.fetchone()[0]

print('Минимальный возраст среди пользователей: ' + str(min_age) + '\n')

# Нахождение максимального возраста
print('Нахождение максимального возраста\n')

cursor.execute('SELECT MAX(age) FROM Users')
max_age: Any = cursor.fetchone()[0]

print('Максимальный возраст среди пользователей: ' + str(max_age) + '\n')

# Находим пользователей с наибольшим возрастом
print('Находим пользователей с наибольшим возрастом\n')

cursor.execute('''
SELECT username, age
FROM Users
WHERE age = (SELECT MAX(age) FROM Users)    
''')
oldest_users: list[Any] = cursor.fetchall()

print_results(oldest_users)

# Выбираем всех пользователей
print('Выбираем всех пользователей\n')

cursor.execute('SELECT * FROM Users')
users: list[Any] = cursor.fetchall()

print_results(users)

# Выбираем первого пользователя
print('Выбираем первого пользователя\n')

cursor.execute('SELECT * FROM Users')
first_user: Any = cursor.fetchone()

print(str(first_user) + '\n')

# Выбираем первых 3 пользователей
print('Выбираем первых 3 пользователей\n')

cursor.execute('SELECT * FROM Users')
first_five_users: list[Any] = cursor.fetchmany(3)

print(str(first_five_users) + '\n')

# Выбираем всех пользователей
print('Выбираем всех пользователей\n')

cursor.execute('SELECT * FROM Users')
all_users: list[Any] = cursor.fetchall()

print(str(all_users) + '\n')

# Выбираем всех пользователей
print('Выбираем всех пользователей\n')

cursor.execute('SELECT * FROM Users')
users: list[Any] = cursor.fetchall()

# Преобразуем результаты в список словарей
print('Преобразуем результаты в список словарей\n')

user_list: list[dict] = []
user: Any
for user in users:
    user_dict: dict = {
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
    }
    user_list.append(user_dict)

print_results(user_list)

# Выбираем пользователей с неизвестным возрастом
print('Выбираем пользователей с неизвестным возрастом\n')

cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unknown_age_users: list[Any] = cursor.fetchall()

print_results(unknown_age_users)

# Использование операторов BEGIN, COMMIT и ROLLBACK
print('Использование операторов BEGIN, COMMIT и ROLLBACK\n')

try:
    # Начинаем транзакцию
    print('Начинаем транзакцию\n')

    cursor.execute('BEGIN')

    # Выполняем операции
    print('Выполняем операции\n')

    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user7', 'user7@example.com'))
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user8', 'user8@example.com'))

    # Подтверждаем изменения
    print('Подтверждаем изменения\n')

    cursor.execute('COMMIT')

except sqlite3.Error:
    # Отменяем транзакцию в случае ошибки
    print('Отменяем транзакцию в случае ошибки\n')

    cursor.execute('ROLLBACK')

# Автоматическое управление транзакциями с помощью контекстных менеджеров
print('Автоматическое управление транзакциями с помощью контекстных менеджеров\n')

with connection:
    # Выполняем операции
    print('Выполняем операции\n')

    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user9', 'user9@example.com'))
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user10', 'user10@example.com'))

# Создаем подготовленный запрос
print('Создаем подготовленный запрос\n')

query: str = 'SELECT * FROM Users WHERE age > ?'
cursor.execute(query, (25,))
users: list[Any] = cursor.fetchall()

print_results(users)

# Сохраняем изменения и закрываем соединение
print('Сохраняем изменения и закрываем соединение\n')

connection.commit()
connection.close()
