import sqlite3
import os
#Функция создания базы данных
#Спасибо https://habrahabr.ru/post/160861/ за пояснение в отношении rowid
def create_db():
    bank = sqlite3.connect("bank.sqlite")
    c = bank.cursor()
    c.execute('''CREATE TABLE money_table (id INTEGER PRIMARY KEY ASC, money int, deposit int, credit int)''')
    bank.commit()
    c.close()
    bank.close()

def chek_db():
    files = os.listdir(".")
    for file in files:
        if file == "bank.sqlite":
            return
    create_db()

#Функция занесения денег в базу
def add_money(money,deposit,credit):
    bank = sqlite3.connect('bank.sqlite')
    c = bank.cursor()
    c.execute("INSERT INTO money_table (money,deposit,credit) VALUES ('%d','%d', '%d')"%(money,deposit,credit))
    bank.commit()
    c.close()
    bank.close()

#Функция вывода информации
def info():
    bank = sqlite3.connect('bank.sqlite')
    c = bank.cursor()
    c.execute('SELECT * FROM money_table')
    row = c.fetchone()
    while row is not None:
        print("id:" + str(row[0]) + " Деньги на счету: " + str(row[1]) + " | На депозите: " + str(row[2]) + " | В кредите: " + str(row[3]))
        row = c.fetchone()
    # закрываем соединение с базой
    c.close()
    bank.close()
