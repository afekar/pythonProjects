import random
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    CHARS_CORRECT = ascii_lowercase + ascii_uppercase + digits+'_.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if cls.correct_email(email):
            return True
        else:
            return False

    @classmethod
    def correct_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count('@') != 1:
            return False
        temp = cls.CHARS_CORRECT+'@'
        for x in email:
            if x not in temp:
                return False
        sobaka_index = email.index('@')
        if sobaka_index > 100:
            return False
        if len(email)-sobaka_index-1 > 50:
            return False
        if email[sobaka_index:].count('.') == 0:
            return False
        if email.count('..') > 0:
            return False
        return True

    @classmethod
    def get_random_email(cls):
        email = ''
        for i in range(random.randint(0, 100)):
            email += random.choice(cls.CHARS_CORRECT)
        email += '@gmail.com'
        return email

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        else:
            return False


print(EmailValidator.check_email("sc..lib@list.ru"))