class Client:

    def __init__(self, name, last_name, pin):
        self.__name = name
        self.__last_name = last_name
        self.__pin = pin

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_pin(self):
        return self.__pin

    def set_name(self, name):
        self.__name = name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_pin(self, pin):
        self.__pin = pin