import sqlite3
import os
import client_manager

#Функция создания базы данных
#Спасибо https://habrahabr.ru/post/160861/ за пояснение в отношении rowid
def create_db():
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE money_table (id Integer PRIMARY KEY ASC, money NUMBER, deposit NUMBER, credit NUMBER)''')
    cursor.execute('''CREATE TABLE client_table (id Integer PRIMARY KEY ASC, name STRING, last_name STRING, pin STRING, operations STRING)''')
    conn.commit()
    cursor.close()
    conn.close()
#id INTEGER PRIMARY KEY ASC, money int, deposit int, credit int
#STRING - использовать для ввода/вывода строк
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

def add_client(name, last_name, pin):
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()

    t = (name, last_name, pin, " ")
    cursor.execute("insert into client_table (name, last_name, pin, operations) values (?, ?, ?, ?)", t)
    client_manager.current_client.set_id(str(cursor.lastrowid))

    conn.commit()
    cursor.close()
    conn.close()

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



def set_operation(operation):
    conn = sqlite3.connect('bank.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM client_table")
    row = cursor.fetchone()
    t = ""
    while row is not None:
        t += str(row[4])
        row = cursor.fetchone()
    t += operation
    cursor.close()
    conn.close()

    conn = sqlite3.connect('bank.sqlite')
    cursor = conn.cursor()
    # Заменяем значение operations в таблице клиента, ориентируясь на его текущий id
    cursor.execute('''SELECT operations FROM client_table WHERE id=?''', (client_manager.current_client.get_id(),))
    example = cursor.fetchone()
    cursor.execute('''UPDATE client_table SET operations = ? WHERE id = ?''', (t,  int(client_manager.current_client.get_id())))
    conn.commit()

    cursor.close()
    conn.close()


#Функция вывода информации
def info():
    conn = sqlite3.connect('bank.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM money_table')
    row = cursor.fetchone()
    while row is not None:
        print("id:" + str(row[0]) + " Деньги на счету: " + str(row[1]) + " | На депозите: " + str(row[2]) + " | В кредите: " + str(row[3]))
        row = cursor.fetchone()

    # закрываем соединение с базой
    cursor.close()
    conn.close()