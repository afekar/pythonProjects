import re
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if re.match('^\d{4}-\d{4}-\d{4}-\d{4}$', number):
            return True
        else:
            return False

    @staticmethod
    def check_name(name):
        if re.match('^[A-Z]+\s[A-Z]+$', name):
            return True
        else:
            return False

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")