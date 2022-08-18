class FloatValue:

    @classmethod
    def check_real(cls, value):
        if type(value) is not float:
            raise TypeError('Присваивать можно только вещественный тип данных')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_real(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, N, M):
        self.cells = [[0] * M for i in range(N)]
        self.init(N, M)

    def init(self, N, M):
        temp = 0.0
        for i in range(N):
            for j in range(M):
                self.cells[i][j] = Cell(temp+float(i*M+j+1))

    def show_table(self):
        cols = len(self.cells[0])
        rows = len(self.cells)
        for i in range(rows):
            for j in range(cols):
                print(self.cells[i][j].value, end=' ')
            print('\n')



table = TableSheet(5, 3)
table.show_table()
