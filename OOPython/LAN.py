class Server:
    next_ip = 0

    def __new__(cls, *args, **kwargs):
        cls.next_ip += 1
        return super().__new__(cls)

    def __init__(self):
        self.buffer = list()
        self.ip = self.next_ip
        self.router = None

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        temp = self.buffer.copy()
        self.buffer.clear()
        return temp

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = list()
        self.server_list = list()

    def link(self, server):
        self.server_list.append(server)
        server.router = self

    def unlink(self, server):
        self.server_list.remove(server)
        server.router = None

    def send_data(self):
        for x in self.buffer:
            self.find_server(x.ip).buffer.append(x)
        self.buffer.clear()

    def find_server(self, ip):
        for x in self.server_list:
            if x.ip == ip:
                return x
        raise ValueError('IP адрес сервера отсуствует в табице маршрутизации')


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print()