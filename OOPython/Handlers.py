#Handler 1
class HandlerGET:

    def __init__(self, func):
        self.__func = func

    def __call__(self, request, *args, **kwargs):
        if 'method' in request.keys():
            if request['method'] is 'GET':
                return self.get(self.__func, request)
            else:
                return None
        else:
            return self.get(self.__func, request)

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'


@HandlerGET
def contact(request):
    return 'Some Info'

#Handler 2
class Handler:
    def __init__(self, methods=('GET',)):
        self.__methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request: dict):
            if self.__check_methods(request):
                method = request['method'].lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def __check_methods(self, request: dict):
        return 'method' in request.keys() and request['method'] in self.__methods

    def get(self, func, request):
        return f'GET: {func(request)}'

    def post(self, func, request):
        return f'POST: {func(request)}'



@Handler(methods=('GET', 'POST'))
def contact(request):
    return 'Some Info'


res = contact({"method": "GET", "url": "contact.html"})
print(res)
res = contact({"method": "POST", "url": "contact.html"})
print(res)
res = contact({})
print(res)

#