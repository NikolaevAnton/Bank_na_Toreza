import service_manager
import data_base_script
import client_manager

def update_db():
    data_base_script.add_money(service_manager.client_money.get_x(),
                               service_manager.deposit.get_money_deposit(),
                               service_manager.credit.get_money_credit())

def receptionist():
    print("Банк на Тореза")
    while 1 > 0:
        print("Ваши действия:")
        print("1 # Сделать вклад.")
        print("2 # Свой вклад я хочу положить под проценты")
        print("3 # То, что я положил под проценты, я хочу вернуть в свой вклад")
        print("4 # Пожалуй, возьму у вас кредит")
        print("5 # Погасить кредит")
        print("6 # Выйти из банка.")
        client_do = 0
        try:
            client_do = int(input("Выбирете вариант: "))
        except ValueError:
            print("Вводите цифру!")

        # Вклад денег на счет
        if client_do == 1:
            service_manager.bank_servise_put()
            update_db()
            continue

         # Расчет вклада под проценты
        elif client_do == 2:
            service_manager.bank_servise_deposit()
            update_db()
            continue

        # Вывод денег, отложенных на депозит на основной счет
        elif client_do == 3:
            service_manager.bank_servose_up_deposit()
            update_db()
            continue

        # Кредитное ярмо
        elif client_do == 4:
            service_manager.bank_servise_credit()
            update_db()
            continue

        # Высвобождение из оного
        elif client_do == 5:
            service_manager.bank_servise_kill_credit()
            update_db()
            continue

        # Выход из метода
        elif client_do == 6:
            break

        else:
            print("Введите корректный вариант, чтобы банковский служащий разобрался с вашей проблемой!")





def main():
    client_manager.name_client()
    receptionist()
    print("У клиента на счету: ", service_manager.client_money.get_x())
    print("Вклад по проценты", service_manager.deposit.get_money_deposit())
    service_manager.money_calc(service_manager.DEPOSIT)
    print("Кредит: ", service_manager.credit.get_money_credit(), " под ", service_manager.credit.get_procent(), "%")
    service_manager.money_calc(service_manager.CREDIT)
    print("История транзакций:")

    data_base_script.info()



if __name__ == "__main__":
    data_base_script.chek_db()
    main()