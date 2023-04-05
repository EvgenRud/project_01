# -*- coding: utf-8 -*-
"""04042023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pk0u2ghgDx4VMXVh6L_A-1PjlVkUF1y2
"""

# Создание БД
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO Teatcher (Teatcher_Id , Teatcher_Name , School_Id, Joining_Date , Speciality , Salary, Experience)
VALUES
('101', 'Галина', '1', '2021 02 10', ' Физик ', '40000', NULL),
('102', 'Мария', '1', '2018 07 23', ' Химик ', '20000', NULL),
('103', 'Ольга', '2', '2022 05 19', 'Информатик', '25000', NULL),
('104', 'Полина', '2', '2017 12 28', 'Физик ', '28000', NULL),
('105', 'Лидия', '3', '2015 06 04', 'Информатик', '42000', NULL),
('106', 'Анастасия', '3', '2019 09 11', 'Учитель трудов', '30000', NULL),
('107', 'Ирина', '4', '2020 08 21', 'Информатик', '32000', NULL),
('108', 'Виктория', '4', '2017 10 17', 'Географ', '30000', NULL);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Задача 2. Подключиться к БД и вывести ее версию
import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_database_version():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT sqlite_version();")
    db_version = cursor.fetchone()
    print ("Вы подключились к SQLite версии: ", db_version)
    close_connection(connection)
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

print ("Задача 2. Подключиться к БД и вывести ее версию")
read_database_version()

# Задача 3. Проставить опыт работы всем учителям
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
update_query ="UPDATE Teatcher SET Experience = 20 WHERE School_Id = 4"
cursor.execute(update_query)
connection.commit()
connection.close()

# Задача 4. Вывести данные о школе и учителе, используя идентификатор школы и идентификатор учителя
import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_detail(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query,(school_id,))
    records = cursor.fetchall()
    print ("Данные по школе")
    for row in records:
      print ("ID школы: ", row[0])
      print ("Название школы: ", row[1])
      print ("Количество мест: ", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)
    
def get_teatcher_detail(teatcher_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Teatcher WHERE Teatcher_Id = ?"""
    cursor.execute(select_query,(teatcher_id,))
    records = cursor.fetchall()
    print ("Данные по учителям")
    for row in records:
      print ("ID Учителя: ", row[0])
      print ("Имя учителя: ", row[1])
      print ("ID школы: ", row[2])
      print ("Дата начала работы: ", row[3])
      print ("Специализация: ", row[4])
      print ("Зарплата: ", row[5])
      print ("Опыт работы: ", row[6])
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

print ("Задача 4 Вывести данные по школе и учителю")
get_school_detail(2)

get_teatcher_detail(107)

# Задача 5. Вывести список учителей по заданной специальности и зарплате
import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_specialist_teatchers_list(speciality, salary):
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Teatcher WHERE Speciality = ? and Salary > ?"""
    cursor.execute(select_query,(speciality, salary))
    records = cursor.fetchall()
    print ("Учителя по специальности", speciality, "и зарплатой больше чем", salary, "\n")
    for row in records:
     print ("ID Учителя: ", row[0])
     print ("Имя учителя: ", row[1])
     print ("ID школы: ", row[2])
     print ("Дата начала работы: ", row[3])
     print ("Специализация: ", row[4])
     print ("Зарплата: ", row[5])
     print ("Опыт работы: ", row[6], "\n")
    close_connection(connection)
 
print ("Задача 5 . Вывести список учителей по заданной специальности и зарплате")
get_specialist_teatchers_list("Информатик",30000)

# Задача 6 . Вывести список учителей по ID школы
import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

def get_teatcher(school_id):
  try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = """SELECT * FROM Teatcher WHERE School_Id = ?"""
    cursor.execute(sql_select_query, (school_id,))
    records = cursor.fetchall()
    print ("Учителя из школы", school_name)
    for row in records:
      print ("ID Учителя: ", row[0])
      print ("Имя учителя: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", school_name)
      print ("Дата начала работы: ", row[3])
      print ("Специализация: ", row[4])
      print ("Зарплата: ", row[5])
      print ("Опыт работы: ", row[6], "\n")
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

print ("Задача 6. Вывести список учителей по ID школы \n")
get_teatcher(1)