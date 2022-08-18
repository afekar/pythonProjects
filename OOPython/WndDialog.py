class WindowDlg:

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.width}, {self.height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check_value(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check_value(height):
            self.__height = height
            self.show()

    @staticmethod
    def check_value(value):
        if type(value) is int and 0 <= value <= 10000:
            return True
        else:
            return False


wnd = WindowDlg('Диалог 1', '100', '50')
wnd.width = 20
wnd.height = 40
