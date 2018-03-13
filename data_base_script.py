import sqlite3
import os
#Функция создания базы данных
#Спасибо https://habrahabr.ru/post/160861/ за пояснение в отношении rowid
def create_db():
    conn = sqlite3.connect("bank.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE money_table (id NUMBER PRIMARY KEY ASC, money NUMBER, deposit NUMBER, credit NUMBER)''')
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
    
    #так делать небезопасно, программа небезопасна к SQL атакам
    #cursor.execute("INSERT INTO money_table (money,deposit,credit) VALUES ('%d','%d', '%d')"%(money,deposit,credit))

    #благонравно использую тюпл, согласно DB-API
    t = (money, deposit, credit)
    cursor.execute("insert into money_table (money,deposit,credit) values (?, ?, ?)", t)

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