import re


class PhoneBook:

    def __init__(self):
        self.number_list = list()

    def add_phone(self, phone):
        self.number_list.append(phone)

    def remove_phone(self, indx):
        self.number_list.pop(indx)

    def get_phone_list(self):
        return self.number_list


class PhoneNumber:

    def __new__(cls, *args, **kwargs):
        if cls.check_new(*args):
            return super().__new__(cls)
        return None

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    @staticmethod
    def check_new(phone, fio):
        if type(phone) is int and re.match('^\d{11}$', str(phone)) and type(fio) is str:
            return True
        else:
            return False