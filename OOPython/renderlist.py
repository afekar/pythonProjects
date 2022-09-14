class RenderList:
    def __init__(self, type_list):
        possible_types = ['ul', 'ol']
        if type_list in possible_types:
            self.__type = type_list
        else:
            self.__type = 'ul'

    def __call__(self, *args, **kwargs):
        temp = '\n'.join([f'<li>{x}</li>' for x in args[0]])
        return f'<{self.__type}>\n{temp}\n</{self.__type}>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList('ol')
html = render(lst)
print(html)