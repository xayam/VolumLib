class Server:
    def __init__(self, controller):
        self.controller = controller
        self.model = controller.model

    def run(self) -> int:
        self.controller.log.info("Сервер запущен")
        input()
        return 0
