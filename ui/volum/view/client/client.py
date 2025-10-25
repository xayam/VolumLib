from volum.view.client.appkivy import AppKivy


class Client(AppKivy):

    def __init__(self, controller):
        AppKivy.__init__(self, controller)

    def run(self) -> int:
        super().run()
        return 0
