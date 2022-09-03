class Server:
    ip_count = 0

    def __init__(self):
        self.buffer = []
        self.ip = int()

    def send_data(self, data, ip) -> None:
        # Router.send_data(data, ip)

    def get_data(self) -> list:
        r_data = self.buffer.copy()
        self.buffer.claer()
        return r_data

    @classmethod
    def get_ip(cls, self):
        cls.ip_count += 1
        self.ip = cls.ip_count
        return self.ip


class Router:
    buffer = []

    @classmethod
    def link(cls, server):
        cls.buffer.append(server)

    @classmethod
    def unlink(cls, server):
        cls.buffer.remove(server)

    @classmethod
    def send_data(cls):
        cls.buffer


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
