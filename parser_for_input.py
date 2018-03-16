import service_manager

# Константы для чтения введенной информации в методе parser_info
ADD_CLIENT = "add client"
ADD_MONEY = "add money"
ADD_CREDIT = "add credit"
ADD_KILL_CREDIT = "add kil credit"
ADD_DEPOSIT = "add deposit"
ADD_KILL_DEPOSIT = "kill deposit"
VALUTE_RUB = "RUB"
VALUTE_DOLLARS = "DOLLARS"
VALUTE_EURO = "EURO"

class Pars:
    def __init__(self, pr1, pr2, pr3, pr4):
        self.__pr1 = pr1
        self.__pr2 = pr2
        self.__pr3 = pr3
        self.__pr4 = pr4

    def set_pr1(self,pr1):
        self.__pr1 = pr1

    def set_pr2(self, pr2):
        self.__pr2 = pr2

    def set_pr3(self, pr3):
        self.__pr3 = pr3

    def set_pr4(self, pr4):
        self.__pr4 = pr4

    def get_pr1(self):
        return self.__pr1

    def get_pr2(self):
        return self.__pr2

    def get_pr3(self):
        return self.__pr3

    def get_pr4(self):
        return self.__pr4

# Инициизирую параметры для парсера
parser = Pars(0,'',0,'')

# код для парсирования строки ввода информации
# Реформа парсера
def parser_info(info, parametrs):

    text = input(info)
    list = text.split()

   #if parametrs == ADD_CLIENT:
   #    text = input(info)
   #    list = text.split()
   #    if list[0] == '' or list[1] == '':
   #        raise ValueError
   #    service_manager.parser.set_pr1(list[0])
   #    service_manager.parser.set_pr2(list[1])
   #    return True
   #
   #elif parametrs == ADD_MONEY:
   #    while 1 > 0:
   #        i = input("выберете валюту: 1 - рубли, 2 - доллары, 3 - евро")





    if parametrs == 3:
        text += " _"



    # Парсинг имени клиента
    if parametrs == 5:
        if list[0] == '' or list[1] == '':
            raise ValueError
        service_manager.parser.set_pr1(list[0])
        service_manager.parser.set_pr2(list[1])
        return True

    try:
        service_manager.parser.set_pr1(int(list[0]))
        if list[1] == '':
            raise ValueError
        service_manager.parser.set_pr2(list[1])
        if parametrs == 4:
            if list[3] == '':
                raise ValueError
            service_manager.parser.set_pr3(int(list[2]))
            service_manager.parser.set_pr4(list[3])
    except ValueError:
        print("банковский служащий: Корректно вводите!")
        return False
    except IndexError:
        print("банковский служащий: Корректно вводите!")
        return False
    return True

def helper_parser(value, parametr):
    if parametr == "add money valute":
        try:
            i = int(value)
            if i == 0 or i < 0 or i > 3:
                return False
            return True
        except ValueError:
            return False