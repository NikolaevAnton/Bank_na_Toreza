import money_manager

# Инициизирую здесь нулевую сумму на счете
client_money = money_manager.Money(0,0)
# Инициилизирую счет под будущий депозит
deposit = money_manager.Deposit(0,0,0)
# Инициизирую параметры для парсера
parser = money_manager.Pars(0,'',0,'')
DEPOSIT = "deposit"
LOW_NOL = "<0"
CHEK_MONEY = "chek money"
UP_DEPOSIT = "up deposit"

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

# Высчитываем сумму с процентами
def money_calc(command):
    if command == DEPOSIT:
        money_deposit = deposit.get_money_deposit()
        i = 0
        while i < deposit.get_yaer():
            money_deposit += money_deposit * deposit.get_procent() / 100
            i += 1
        print("Через ", deposit.get_yaer(), " под процентами ", deposit.get_procent(), " на вашем счету окажется: ", money_deposit)

def chek_summ(command):
    if command == LOW_NOL:
        if parser.get_pr1() < 0:
            print("Не надо вводить отрицательные суммы!")
            # Обезвреживание отрицательной суммы
            parser.set_pr1(0)
            return False
        else:
            return True
    elif command == CHEK_MONEY:
        if client_money.get_x() == 0:
            print("банковский служащий: банковский служащий: сделайте первый взнос, у вас на счету 0!")
            parser.set_pr1(0)
            return False
        else:
            return True
    elif command == UP_DEPOSIT:
        if parser.get_pr1() > client_money.get_x():
            print("сумма того что вы хотите положить под проценты больше количества ваших денег!")
            parser.set_pr1(0)
            return False
        else:
            return True

# Функции действий банковского служащего
def bank_servise_put():
    print("Сколько вы хотите положить денег?")
    while 1 > 0:
        if parser_info("Вводите деньги в формате: 100 RUB", 2):
            if chek_summ(LOW_NOL):
                client_money.summ(parser.get_pr1())
                print("Вы положили на свой счет: ", client_money.get_x())
                break
            else:
                continue

def bank_servise_deposit():
    while 1 > 0:
        if not chek_summ(CHEK_MONEY):
            answer = input("Хотите сделать первый взнос? Y/N")
            if answer == "Y":
                bank_servise_put()
                continue
            else:
                break
        print("банковский служащий: Выбирете процентную ставку и время вклада")
        while 1 > 0:
            if not parser_info("банковский служащий: введите данные в формате 5 % 2 года", 4):
                continue
            else:
                break
        print("На вашем счету сейчас ", client_money.get_x())
        print("На депозите: ", deposit.get_money_deposit())
        deposit.set_procent(parser.get_pr1())
        deposit.set_year(parser.get_pr3())

        while 1 > 0:
            if parser_info("банковский служащий: сколько класть на депозит? от 0 до максимума на вашем счете", 3):

                if not chek_summ(UP_DEPOSIT):
                    continue
                elif not chek_summ(LOW_NOL):
                    continue
                elif deposit.get_yaer() == 0:
                    print("банковский служащий: За такой период вклад не вырастет!")
                    continue
                else:
                    # блок перемешения денег между счетами
                    client_money.minus(parser.get_pr1())
                    deposit.set_money_depost(parser.get_pr1() + deposit.get_money_deposit())
                    print("расчет процентов")
                    money_calc(DEPOSIT)
                    break
        break # конец цикла в начале функции

def bank_servose_up_deposit():
    while 1 > 0:
        if deposit.get_money_deposit() == 0:
            print("банковский служащий: сделайте первый взнос на депозит, у вас на счету 0")
            bank_servise_deposit()
            continue
        print("банковский служащий: на вашем депозите ", deposit.get_money_deposit())
        while 1 > 0:
            if parser_info("Введите сумму, которую нужно перевести с вашего депозита на основной счет", 3):

                if not chek_summ(LOW_NOL):
                    continue

                if parser.get_pr1() > deposit.get_money_deposit():
                    print("Сумма, которую вы хотите вывести из депозита больше, чем есть на депозите!")
                    continue
                deposit.set_money_depost(deposit.get_money_deposit() - parser.get_pr1())
                client_money.set_x(client_money.get_x() + parser.get_pr1())
                print("банковский служащий: баланс ваших счетов ", client_money.get_x(), " основной счет # ",
                      deposit.get_money_deposit(), " депозит")
                break
        break