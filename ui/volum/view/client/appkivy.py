from kivy.config import Config
# from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp as KivyApp

from volum.view.client.main.main import MainScreen


# from volum.view.client.main.loader import LoaderScreen

# Builder.load_file(
#     "volum/view/client/appkivy.kv"
# )


class Windows(MDScreenManager):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class AppKivy(KivyApp):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.model = self.controller.model

        Config.set("kivy", "window_icon", self.model.ICON_PNG)
        self.windows = Windows()
        # windows.add_widget(FirstScreen(name="FirstScreen"))
        # windows.add_widget(SecondScreen(name="SecondScreen"))
        self.main_window = MainScreen(self.controller)
        self.windows.add_widget(self.main_window)
        self.controller.container = self.windows

    def build(self):
        self.icon = self.model.ICON_PNG
        self.title = self.model.app_header()
        # self.controller.container.size_hint = (1, 1)
        return self.controller.container

    def on_start(self):
        pass
        # self.controller.container.tab_width = 3 * self.controller.container.tab_height
        # self.controller.catalog.on_resize()
