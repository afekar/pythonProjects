class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        possible_types = {'title': str, 'author': str, 'pages': int, 'year': int}
        if possible_types[key] != type(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
print(book.__dict__)