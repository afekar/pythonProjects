class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.__min_length = min_length
        self.__max_length = max_length

    def validate(self, string):
        return type(string) is str and self.__min_length <= len(string) <= self.__max_length


class RegisterForm:

    login = StringValue(ValidateString())
    password = StringValue(ValidateString())
    email = StringValue(ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f"<form>Логин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>")


rf = RegisterForm('Example_login', 'qwerty', 'qwerty@mail.ru')
print(rf.__dict__)
rf.show()
print(rf.get_fields())
