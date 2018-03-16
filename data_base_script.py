import sqlite3
import os
import client_manager

#Функция создания базы данных
#Спасибо https://habrahabr.ru/post/160861/ за пояснение в отношении rowid
def create_db():
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE money_table (id Integer PRIMARY KEY ASC, money NUMBER, deposit NUMBER, credit NUMBER)''')
    cursor.execute('''CREATE TABLE client_table (id Integer PRIMARY KEY ASC, name STRING, last_name STRING, pin STRING)''')
    conn.commit()
    cursor.close()
    conn.close()

# Пин год вводятся цифрами и переводится в строку. Где-то теряются нули в начале пинкода
# если они там были
def pin_four(pin):
    pincode = str(pin)
    if len(pincode) == 0:
        return "0000"
    elif len(pincode) == 1:
        return "000"+pincode
    elif len(pincode) == 2:
        return "00"+pincode
    elif len(pincode) == 3:
        return "0"+pincode
    else:
        return pincode

# Самая первая функция, вызываемая из main()
# проверяет, есть ли база данных. Если нет - создает
def chek_db():
    files = os.listdir(".")
    for file in files:
        if file == "bank.sqlite":
            return
    create_db()

#Функция занесения денег в базу
def add_money(money,deposit,credit):
    conn = sqlite3.connect('bank.sqlite')
    cursor = conn.cursor()
    # Передаем информацию о последней операции в базу данных клиента

    #благонравно использую тюпл, согласно DB-API
    t = (money, deposit, credit)
    cursor.execute("insert into money_table (money,deposit,credit) values (?, ?, ?)", t)
    operation = str(cursor.lastrowid)
    conn.commit()
    cursor.close()
    conn.close()
    set_operation(operation)

# добавдение информации о клиенте в таблицу client_name
def add_client(name, last_name, pin):
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()
    t = (name, last_name, pin)
    cursor.execute("insert into client_table (name, last_name, pin) values (?, ?, ?)", t)
    client_manager.current_client.set_id(str(cursor.lastrowid))
    conn.commit()
    cursor.close()
    conn.close()
    create_table_for_client_operation(None,pin) # создаем пустую таблицу транзакций клиента

# Создаем список имеющихся клиентов
def list_clients_pin_in_DB():
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM client_table")
    row = cursor.fetchone()
    while row is not None:
        id = row[0]
        name = row[1]
        last_name = row[2]
        pin = row[3]
        info_list = [id, name, last_name, pin]
        client_manager.client_ids.append(info_list)
        row = cursor.fetchone()
    cursor.close()
    conn.close()

# Создание таблицы на клиента в формате name_client_пин. Также
# добавляем туда id операции, чтобы в последующем из таблицы money_table
# взять значения транзакций
def create_table_for_client_operation(operation, pin):

    name_client_operation = "name_client_" + str(pin)
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()
    sql_command = ("CREATE TABLE " + name_client_operation +" (id Integer PRIMARY KEY ASC, id_operation STRING)")
    cursor.execute(sql_command)
    sql_command = ("INSERT INTO " + name_client_operation + " (id_operation) VALUES(?)")
    cursor.execute(sql_command, (operation,))
    conn.commit()
    cursor.close()
    conn.close()

# Добавляем во вспомогательную таблицу пользователь - транзакция информацию про id операции с деньгами
# Если такой таблицы нет - создаем ее. Не знаю, корректно ли создавать для каждого пользователя
# свою таблицу, но так нагляднее и проще, чем писать номера операций в формате _1_2_3_18 в специальном поле
# в таблице client_table в каком либо дополнительном поле
def set_operation(operation):
    pin = pin_four(client_manager.current_client.get_pin())
    name_client_operation = "name_client_" + str(pin)
    # проверка есть ли клиент в бд
    try:
        conn = sqlite3.connect("bank.sqlite")
        cursor = conn.cursor()
        sql_command = ("SELECT * FROM " + name_client_operation)
        cursor.execute(sql_command)
        # Таблица пользователя есть раз дошли до этой строчки, добваляем в нее поля
        sql_command = ("INSERT INTO " + name_client_operation + "(id_operation) values (?)")
        cursor.execute(sql_command, (operation,))
        conn.commit()
        cursor.close()
        conn.close()

    except sqlite3.OperationalError:
        # Таблицы пользователя нет, создаем
        create_table_for_client_operation(operation, pin)


#Функция вывода информации
def info():
    # Выводим информацию для текущего пользователя
    pin = pin_four(client_manager.current_client.get_pin())
    list_ids = []
    conn = sqlite3.connect('bank.sqlite')
    cursor = conn.cursor()
    sql_command = ("SELECT * FROM name_client_" + pin)
    cursor.execute(sql_command)
    row = cursor.fetchone()
    while row is not None:
        list_ids.append(row[1])
        row = cursor.fetchone()
    cursor.close()
    conn.close()

    conn = sqlite3.connect('bank.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM money_table')
    row = cursor.fetchone()
    print("История транзакций для " + client_manager.full_info_client())
    i = 1
    while row is not None:

        if super_any(list_ids,row[0]):
            print("№:" + str(i) + " Внесение денег на счет: " + str(row[1]) + " | На депозит: " + str(
                row[2]) + " | В кредит: " + str(row[3]))
            i += 1

        row = cursor.fetchone()

    cursor.close()
    conn.close()

# вспомогательная функция для проверки есть ли какое значение в списке
def super_any(list_ids, id):
    for idx in list_ids:
        if idx == id:
            return True

    return False