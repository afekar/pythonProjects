from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = ''
        self.size = size
        if self.check_name(name):
            self.name = name

    def get_html(self):
        return str(f"<p class='login'>{self.name}: <input type='text' size={self.size} />")

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and cls.check_str(name):
            return True
        else:
            raise ValueError("некорректное поле name")

    @classmethod
    def check_str(cls, string):
        for x in string:
            if x not in cls.CHARS_CORRECT:
                return False
        return True


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = ''
        self.size = size
        if self.check_name(name):
            self.name = name

    def get_html(self):
        return str(f"<p class='password'>{self.name}: <input type='text' size={self.size} />")

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and cls.check_str(name):
            return True
        else:
            raise ValueError("некорректное поле name")

    @classmethod
    def check_str(cls, string):
        for x in string:
            if x not in cls.CHARS_CORRECT:
                return False
        return True


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()