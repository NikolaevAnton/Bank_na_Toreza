import service_manager

def receptionist():
    print("Банк на Тореза")
    while 1 > 0:
        print("Ваши действия:")
        print("1 # Сделать вклад.")
        print("2 # Свой вклад я хочу положить под проценты")
        print("3 # То, что я положил под проценты, я хочу вернуть в свой вклад")
        print("5 # Выйти их приложения.")
        client_do = 0
        try:
            client_do = int(input("Выбирете вариант: "))
        except ValueError:
            print("Вводите цифру!")

        # Вклад денег на счет
        if client_do == 1:
            service_manager.bank_servise_put()
            continue

         # Расчет вклада под проценты
        elif client_do == 2:
            service_manager.bank_servise_deposit()
            continue

        # Вывод денег, отложенных на депозит на основной счет
        elif client_do == 3:
            service_manager.bank_servose_up_deposit()
            continue

        # Выход из метода
        elif client_do == 5:
            break

        else:
            print("Введите корректный вариант, чтобы банковский служащий разобрался с вашей проблемой!")


def main():
    receptionist()
    print("У клиента на счету: ", service_manager.client_money.get_x())
    print("Вклад по проценты", service_manager.deposit.get_money_deposit())
    service_manager.money_calc("deposit") # лучше здесь смотрелась бы глобальная константа





if __name__ == "__main__":
    main()