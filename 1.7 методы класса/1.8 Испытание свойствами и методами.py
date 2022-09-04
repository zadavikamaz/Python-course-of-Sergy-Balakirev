class Server:
    ip_counter = 0

    def __new__(cls, *args, **kwargs):
        cls.ip_counter += 1
        return super(Server, cls).__new__(cls)

    def __init__(self):
        self.buffer = list()  # contains a class link
        self.ip = self.ip_counter

    @staticmethod
    def send_data(data):
        Router.buffer.append(data)  # write Data(data, ip) link on Router.buffer

    def get_data(self):
        tmp = self.buffer.copy()
        self.buffer = []
        # print(tmp)
        return tmp

    def get_ip(self):
        return self.ip


class Router:
    buffer = list()  # contains data class link,
    server_list = dict()  # dict ip: link to Server

    @classmethod
    def link(cls, server):
        cls.server_list.setdefault(server.get_ip(), server)

    @classmethod
    def unlink(cls, server):
        del cls.server_list[server.get_ip()]

    @classmethod
    def send_data(cls):
        for ip, data in cls.buffer.items():
            cls.server_list[ip].buffer = data
        cls.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()  # new ip = 1
sv_from2 = Server()  # new ip = 2
router.link(sv_from)
router.link(sv_from2)
router.link(Server())  # new ip = 3
router.link(Server())  # new ip = 4
sv_to = Server()  # new ip = 5
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))  # senda data from ip = 1 to ip = 5
sv_from2.send_data(Data("Hello", sv_to.get_ip()))  # send data from ip = 2 to ip = 5
sv_to.send_data(Data("Hi", sv_from.get_ip()))  # send data from ip = 5 to ip = 1
router.send_data()
msg_lst_from = sv_from.get_data()  # msg_lst_from[0].data == "Hi"
msg_lst_to = sv_to.get_data()

print(msg_lst_from[0])
print(msg_lst_to)
