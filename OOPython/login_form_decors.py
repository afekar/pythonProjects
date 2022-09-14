from string import ascii_lowercase, digits


class CharsValidator:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, string='', *args, **kwargs):
        return all(map(lambda x: x in self.__chars, string))


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, string='', *args, **kwargs):
        return self.__min_length <= len(string) <= self.__max_length


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
        return True


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "rootme"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")