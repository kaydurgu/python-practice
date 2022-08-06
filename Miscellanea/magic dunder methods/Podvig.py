class Server:

    _ip = 0
    def __init__(self) -> None:
        self.ip = Server._ip + 1
        Server._ip += 1
        self.buffer = []
        self.Router = None

    def send_data(self, data):
        self.Router.buffer.append(data)

    def get_data(self):
        k = self.buffer[::]
        self.buffer.clear()
        return k

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self) -> None:
        self.servers = {}
        self.buffer = []

    def link(self, server:Server):
        server.Router = self
        self.servers[server.ip] = server
    
    def unlink(self, server:Server):
        server.Router = None
        del self.servers[server.ip]

    def send_data(self):
        for x in self.buffer:
            if self.servers.get(x.recipent_ip):
                self.servers[x.recipent_ip].buffer.append(x)
        self.buffer.clear()


class Data:

    def __init__(self, data, recipent_ip) -> None:
        self.data = data
        self.recipent_ip = recipent_ip

assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

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

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"