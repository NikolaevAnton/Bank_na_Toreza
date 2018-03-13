import service_manager
import data_base_script
import random

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
            continue

         # Расчет вклада под проценты
        elif client_do == 2:
            service_manager.bank_servise_deposit()
            continue

        # Вывод денег, отложенных на депозит на основной счет
        elif client_do == 3:
            service_manager.bank_servose_up_deposit()
            continue

        # Кредитное ярмо
        elif client_do == 4:
            service_manager.bank_servise_credit()
            continue

        # Высвобождение из оного
        elif client_do == 5:
            service_manager.bank_servise_kill_credit()
            continue

        # Выход из метода
        elif client_do == 6:
            break

        else:
            print("Введите корректный вариант, чтобы банковский служащий разобрался с вашей проблемой!")

def chek_pin(pin):
    i = 0
    for p in pin:
        if not p.isdigit():
            print("В пин-коде должны быть только цифры!")
            return False
        i = i + 1
    if i > 4:
        print("В пин-коде должно быть только 4 числа")
        return False
    return True

def pin_generate():
    i = 0
    pin = ""
    while i < 4:
        pin += str(random.randint(0,9))
        i += 1

    # Здесь нужно будет сделать запрос в БД, есть ли такой pin. Если есть - еще раз рекурсивно выполнить pin_generate()

    return pin

def create_client():
    print(" ### Регистрация  клиента банка ###")
    while 1 > 0:
        if service_manager.parser_info("Введите ваше имя и фамилию разделенные пробелом # ", 5):
            # Запоминаем в оперативной памяти клиента
            service_manager.client.set_name(service_manager.parser.get_pr1())
            service_manager.client.set_last_name(service_manager.parser.get_pr2())
            # Генерируем пин-код
            service_manager.client.set_pin(pin_generate())

            print(" ### Ваши параметры ###")
            print(" Имя: ", service_manager.client.get_name())
            print(" Фамилия: ", service_manager.client.get_last_name())
            print(" Пин код: ", service_manager.client.get_pin())
            answer = input("Y/N")
            if answer == "Y":
                break


def name_client():
    print("Введите ваш пинкод, в банке все хотят знать кто вы такой.")
    while 1>0:
        answer = input("Введите 4 цифры вашего пин-кода или выберете N для выхода из банка # ")
        if answer == "N":
            exit(0)
        elif chek_pin(answer):

            # Здесь реализую запрос в бд data_base_script.че-то-там, чтобы знать есть ли такой клиент с таким пинкодом
            # Если есть, прекращаем цикл

            print("Такого клинта нет в нашей базе. Хотите стать клиентом нашего банка?")
            answer = input("Y/N # ")
            if answer == "Y":

                # функция создания клиента с генерацией пинкода
                create_client()
                # запись данных в объект клиент
                # выход из функции
                break

            else:
                exit(0)



def main():
    name_client()
    receptionist()
    print("У клиента на счету: ", service_manager.client_money.get_x())
    print("Вклад по проценты", service_manager.deposit.get_money_deposit())
    service_manager.money_calc(service_manager.DEPOSIT)
    print("Кредит: ", service_manager.credit.get_money_credit(), " под ", service_manager.credit.get_procent(), "%")
    service_manager.money_calc(service_manager.CREDIT)
    data_base_script.add_money(service_manager.client_money.get_x(),service_manager.deposit.get_money_deposit(),service_manager.credit.get_money_credit())
    print("История транзакций:")

    data_base_script.info()



if __name__ == "__main__":
    data_base_script.chek_db()
    main()