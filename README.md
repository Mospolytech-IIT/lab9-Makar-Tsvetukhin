Цель работы:

Освоить основные принципы работы с базой данных через SQLAlchemy: подключение к базе данных, создание таблиц, выполнение запросов и интеграция с веб-приложением.

Задание:

Часть 1: Подключение к базе данных и создание таблиц

Выбор базы данных:
Выберите одну из баз данных: MSSQL, SQLite, PostgreSQL, MySQL.
Установите необходимые библиотеки для работы с выбранной базой данных и SQLAlchemy.

Установка SQLAlchemy

![image](https://github.com/user-attachments/assets/485452fb-8d08-467b-ade0-266b4a1ccdc4)

Создание модели данных:
Опишите модель данных, состоящую из двух таблиц: Users и Posts.
Таблица Users должна содержать следующие поля:
id (целое число, первичный ключ, автоинкремент)
username (строка, уникальное значение)
email (строка, уникальное значение)
password (строка)
Таблица Posts должна содержать следующие поля:
id (целое число, первичный ключ, автоинкремент)
title (строка)
content (текст)
user_id (целое число, внешний ключ, ссылающийся на поле id таблицы Users)
Создание таблиц:
Напишите программу на Python, которая подключается к выбранной базе данных и создает таблицы Users и Posts на основе описанной модели данных.

![image](https://github.com/user-attachments/assets/6cfaf13f-8df1-4cec-98d6-000fda0c1278)

![image](https://github.com/user-attachments/assets/fc7cb139-cca3-43e2-8ffe-1b454ef69d92)

Часть 2: Взаимодействие с базой данных

Добавление данных:
Напишите программу, которая добавляет в таблицу Users несколько записей с разными значениями полей username, email и password.
Напишите программу, которая добавляет в таблицу Posts несколько записей, связанных с пользователями из таблицы Users.

![image](https://github.com/user-attachments/assets/9b0ba2d4-5018-492f-ad19-06f42acaed52)

![image](https://github.com/user-attachments/assets/e139d4ff-b2b1-4f6b-bc9d-03b4472a8622)

![image](https://github.com/user-attachments/assets/414d8a35-944b-42b3-8418-e81a04437070)


Извлечение данных:
Напишите программу, которая извлекает все записи из таблицы Users.
Напишите программу, которая извлекает все записи из таблицы Posts, включая информацию о пользователях, которые их создали.
Напишите программу, которая извлекает записи из таблицы Posts, созданные конкретным пользователем.

![image](https://github.com/user-attachments/assets/33a7e8c3-312d-409a-98c6-5e0585edd4bb)

![image](https://github.com/user-attachments/assets/bed0fae3-23c1-4965-a367-f1ba1a927048)

Обновление данных:
Напишите программу, которая обновляет поле email у одного из пользователей.
Напишите программу, которая обновляет поле content у одного из постов.

![image](https://github.com/user-attachments/assets/96975dd1-1ecb-4e61-8c00-763a6dfef5ce)

![image](https://github.com/user-attachments/assets/34fb9af0-f8c2-4e13-ad8a-54ad3961d68e)

![image](https://github.com/user-attachments/assets/4b165825-3926-46af-940e-519a0a403bff)

Удаление данных:
Напишите программу, которая удаляет один из постов.
Напишите программу, которая удаляет пользователя и все его посты.

![image](https://github.com/user-attachments/assets/246fa604-279e-4c60-83ec-87be12910ae3)

![image](https://github.com/user-attachments/assets/18662d34-902d-4342-840b-7191593000b0)

![image](https://github.com/user-attachments/assets/d1e69aa8-3093-4295-8fa9-596413cba1dd)

Часть 3: Базовые операции с базой данных в веб-приложении

Создание веб-приложения:
Создайте простое веб-приложение на FastAPI.
Интегрируйте SQLAlchemy в ваше веб-приложение.
Реализация CRUD-операций:
Реализуйте веб-страницы для выполнения CRUD-операций (создание, чтение, обновление, удаление) с записями в таблицах Users и Posts.
Страницы должны включать:
Форму для создания нового пользователя/поста.
Список всех пользователей/постов с возможностью редактирования и удаления.
Страницу для редактирования информации о пользователе/посте.

Создал фомры Html для веб приложения:

![image](https://github.com/user-attachments/assets/6ba880c2-1b41-42d9-b7fd-300b74c486e4)

![image](https://github.com/user-attachments/assets/01418dce-8335-4cb3-85db-03bd66ea098d)

![image](https://github.com/user-attachments/assets/87274226-3ab7-4271-a110-74cfa472aa18)


![image](https://github.com/user-attachments/assets/b741117c-0c6b-4ff5-a7d3-b6d51573ca12)

![image](https://github.com/user-attachments/assets/66eadc27-9ab9-46f9-b627-30b2c04db0dd)

![image](https://github.com/user-attachments/assets/e5beb9ca-8d61-4557-a16b-abeb16369c8e)


И отредактировал функции для работы не сконсолью и прярм взаимодействием с бд, а как для веб приложения:

![image](https://github.com/user-attachments/assets/6a1ad8e1-ef7a-4806-a86b-2d1096cfb60f)

![image](https://github.com/user-attachments/assets/3bba5c64-b4d9-4307-b1cb-25b4fcefebd8)

![image](https://github.com/user-attachments/assets/c5462aef-87cd-4fdb-a00e-13a18c62506d)

![image](https://github.com/user-attachments/assets/e5835301-d763-4180-8dd4-6cc1394f93ba)

![image](https://github.com/user-attachments/assets/f7e72d98-dd39-4ce3-b8ca-8d41769b0f97)


Везде также есть функционал удаления и редактирования
