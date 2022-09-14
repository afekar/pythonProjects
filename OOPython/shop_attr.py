class Shop:

    def __init__(self, title):
        self.title = title
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    cur_id = 0

    def __init__(self, name='', weight=0.0, price=0.0):
        self.increase_cnt()
        self.id = self.cur_id
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def increase_cnt(cls):
        cls.cur_id += 1

    @staticmethod
    def check_value(possible_type, value):
        if not any(map(lambda x: x == type(value), possible_type)):
            return False
        if type(value) in (int, float):
            return value >= 0
        return True

    def __setattr__(self, key, value):
        possible_types = {'id': [int], 'name': [str], 'weight': [int, float], 'price': [int, float]}
        if not self.check_value(possible_types[key], value):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")