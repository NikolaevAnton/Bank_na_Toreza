class Money:
    def __init__(self,x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def summ(self,sum):
        self.__x += sum

    def minus(self,min):
        self.__x -= min

class Deposit:
    def __init__(self, money_deposit, procent, time):
        self.__money_deposit = money_deposit
        self.__procent = procent
        self.__time = time

    def set_money_depost(self, money_deposit):
        self.__money_deposit = money_deposit

    def get_money_deposit(self):
        return self.__money_deposit

    def set_procent(self, procent):
        self.__procent = procent

    def get_procent(self):
        return self.__procent

    def set_year(self, time):
        self.__time = time

    def get_yaer(self):
        return self.__time

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