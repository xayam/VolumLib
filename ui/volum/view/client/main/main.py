from volum.view.client.main.mainview import MainView


class MainScreen(MainView):

    def __init__(self, controller):
        self.controller = controller
        self.params = {
            "controller": self.controller,
            "model": self.controller.model,
            "on_press": self.on_press,
        }
        MainView.__init__(self, self.params)

    def on_press(self, _):
        pass
        # self.manager.current = "settings"
