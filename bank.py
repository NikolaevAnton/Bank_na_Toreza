import money_manager

# Инициизирую здесь нулевую сумму на счете
client_money = money_manager.Money(0,0)
# Инициилизирую счет под будущий депозит
deposit = money_manager.Deposit(0,0,0)
# Инициизирую параметры для парсера
parser = money_manager.Pars(0,'',0,'')

# код для парсирования строки ввода информации
def parser_info(info, parametrs):
    text = input(info)
    if parametrs == 3:
        text += " _"
    list = text.split()
    try:
        parser.set_pr1(int(list[0]))
        if list[1] == '':
            raise ValueError
        parser.set_pr2(list[1])
        if parametrs == 4:
            if list[3] == '':
                raise ValueError
            parser.set_pr3(int(list[2]))
            parser.set_pr4(list[3])
    except ValueError:
        print("банковский служащий: Корректно вводите!")
        return False
    except IndexError:
        print("банковский служащий: Корректно вводите!")
        return False
    return True


def receptionist():
    print("Банк на Тореза")
    while 1 > 0:
        print("Ваши действия:")
        print("1 # Сделать вклад.")
        print("2 # Свой вклад я хочу положить под проценты")
        print("5 # Выйти их приложения.")
        client_do = 0
        try:
            client_do = int(input("Выбирете вариант: "))
        except ValueError:
            print("Вводите цифру!")

        # Вклад денег на счет
        if client_do == 1:
            print("Сколько вы хотите положить денег?")
            if parser_info("Вводите деньги в формате: 100 RUB",2):
                client_money.summ(parser.get_pr1())
                print("Вы положили на свой счет: ", client_money.get_x())
                continue
            else:
                continue

         # Расчет вклада под проценты
        elif client_do == 2:
            if client_money.get_x() == 0:
                print("банковский служащий: сделайте первый взнос, у вас на счету 0")
                continue
            print("банковский служащий: Выбирете процентную ставку и время вклада")
            parser_info("банковский служащий: введите данные в формате 5 % 2 года",4)
            print("На вашем счету сейчас ", client_money.get_x())
            print("На депозите: ", deposit.get_money_deposit())
            procent = parser.get_pr1()
            time = parser.get_pr3()
            if parser_info("банковский служащий: сколько класть на депозит? от 0 до максимума на вашем счете",3):
                print("расчет процентов")
                if parser.get_pr1() > client_money.get_x():
                    print("сумма того что вы хотите положить под проценты больше количества ваших денег!")
                    continue
                elif time == 0:
                    continue
                else:
                    client_money.minus(parser.get_pr1())
                    deposit.set_money_depost(parser.get_pr1() + deposit.get_money_deposit())
                    money_deposit = deposit.get_money_deposit()
                    i = 0
                    while i < time:
                        money_deposit += money_deposit * procent / 100
                        i += 1
                    print("Через ", time, " под процентами ", procent, " на вашем счету окажется: ", money_deposit)
                    deposit.set_money_depost(money_deposit)
                    deposit.set_procent(procent)
                    deposit.set_year(time)
                    continue

        elif client_do == 5:
            break
        else:
            print("Введите корректный вариант, чтобы банковский служащий разобрался с вашей проблемой!")


        print("Закончить работу на ресепшене?")
        answer = input("Y/N")
        if answer == "Y":
            break

def main():
    receptionist()
    print("У клиента на счету: ", client_money.get_x())
    print("Вклад. Расчитываемые деньги: ", deposit.get_money_deposit())
    print("Под ",deposit.get_procent(), "% На ", deposit.get_yaer())





if __name__ == "__main__":
    main()