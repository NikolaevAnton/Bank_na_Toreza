import random
import service_manager
import data_base_script

class Client:

    def __init__(self, id, name, last_name, pin, operations):
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__pin = pin
        self.__operations = operations

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_pin(self):
        return self.__pin

    def get_operations(self):
        return self.__operations

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_pin(self, pin):
        self.__pin = pin

    def set_operations(self, operations):
        self.__operations = operations

    def add_operations(self, operations):
        self.__operations += self.__operations + " " + operations + " "

client_ids = []
current_client = Client(0,"","","","")


def full_info_client():
    return current_client.get_name() + " " + current_client.get_last_name() + \
           " # Пин код: " + str(current_client.get_pin()) + " #"

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
    f = 0

    pin = ""
    while True:
        i = 0
        while i < 4:
            pin += str(random.randint(0, 9))
            i += 1

        if not check_client(pin):
            break
        # Тут думаю для того, чтобы избежать бесконечного цикла в случае когда все пинкоды заняты,
        #  надо высчитать максимальное количестов попыток.
        if f == 10000:
            print("Количество пользователей превышает возможности данного банка. (")
            exit(0)
        f += 1
    return pin

def create_client():
    print(" ### Регистрация  клиента банка ###")
    while 1 > 0:
        if service_manager.parser_info("Введите ваше имя и фамилию разделенные пробелом # ", 5):
            # Запоминаем в оперативной памяти клиента
            current_client.set_name(service_manager.parser.get_pr1())
            current_client.set_last_name(service_manager.parser.get_pr2())
            # Генерируем пин-код
            current_client.set_pin(pin_generate())

            print(" ### Ваши параметры ###")
            print(" Имя: ", current_client.get_name())
            print(" Фамилия: ", current_client.get_last_name())
            print(" Пин код: ", current_client.get_pin())
            answer = input("Y/N")
            if answer == "Y":
                data_base_script.add_client(
                    current_client.get_name(),
                    current_client.get_last_name(),
                    current_client.get_pin()
                )
                break

def check_client(pin):
    if len(client_ids) == 0:
        print("База данных клиентов пуста")
        return False
    for client in client_ids:
        if int(client[3]) == int(pin):
            current_client.set_id(client[0])
            current_client.set_name(client[1])
            current_client.set_last_name(client[2])
            current_client.set_pin(client[3])
            return True
    return False

def name_client():
    data_base_script.list_clients_pin_in_DB()
    print("Введите ваш пинкод, в банке все хотят знать кто вы такой.")
    while 1>0:
        answer = input("Введите 4 цифры вашего пин-кода или выберете N для выхода из банка # ")
        if answer == "N":
            exit(0)
        elif chek_pin(answer):

            # Здесь реализую запрос в бд data_base_script, чтобы знать есть ли такой клиент с таким пинкодом
            # Если есть, прекращаем цикл
            if check_client(answer):
                break

            print("Такого клинта нет в нашей базе. Хотите стать клиентом нашего банка?")
            answer = input("Y/N # ")
            if answer == "Y":

                # функция создания клиента с генерацией пинкода
                create_client()

                # выход из функции
                break

            else:
                exit(0)

    print("Здравствуйте ", current_client.get_name(), " ", current_client.get_last_name(), "!")