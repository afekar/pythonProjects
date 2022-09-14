class StringValue:

    def __init__(self, min_length=0, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)

    def check_value(self, value):
        if type(value) is str:
            return self.min_length <= len(value) <= self.max_length
        else:
            return False


class PriceValue:

    def __init__(self, max_value=0.0):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)

    def check_value(self, value):
        if type(value) in (int, float):
            return 0 <= value <= self.max_value
        else:
            return False


class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:

    name = StringValue(2, 50)
    price = PriceValue(1e4)

    def __init__(self, name, price):
        self.name = name
        self.price = price
