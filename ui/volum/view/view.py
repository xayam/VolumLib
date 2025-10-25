from volum.entity import *
from volum.i18l.messages import *


class View:
    controller = None
    model = None

    def __init__(self):
        pass

    def run(self) -> str:
        if self.controller.query.target == TARGET_SERVER:
            from volum.view.server.server import Server
            Server(self.controller).run()
            return "Exit"
        elif self.controller.query.target == TARGET_CLIENT:
            from volum.view.client.client import Client
            Client(self.controller).run()
            return "Exit"
        else:
            raise Exception(self.controller.log.error(self.model.i18l.t(TARGET_UNKNOWN_)))
