from kivy.uix.actionbar import ActionBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter
from kivymd.uix.screen import MDScreen

from volum.view.client.main.left import Left
from volum.view.client.main.right import Right


class MainView(MDScreen):

    def __init__(self, param: dict):
        self.param = param
        MDScreen.__init__(self)

        self.root = BoxLayout(orientation="vertical")
        self._layout_header()
        self._layout_main()
        self._layout_status()
        self.layout_left = Left(self.layout_left_view)
        self.layout_right = Right(self.layout_right_view)
        self.add_widget(self.root)

        self.theme_cls.theme_style = self.param["model"].theme_style

    def _layout_main(self):
        layout_main = BoxLayout()

        self.layout_left_view = BoxLayout()
        self.layout_right_view = BoxLayout(orientation="vertical")

        splitter = Splitter(sizable_from="right")
        splitter.size_hint = (None, 1)
        splitter.size = (250, 0)
        splitter.min_size = '70pt'
        splitter.max_size = '600pt'
        splitter.add_widget(self.layout_left_view)
        splitter.strip_size = '5pt'
        layout_main.add_widget(splitter)
        layout_main.add_widget(self.layout_right_view)
        self.root.add_widget(layout_main)

    def _layout_header(self):
        self.layout_header_view = BoxLayout()
        self.layout_header_view.size_hint = (1, None)
        self.layout_header_view.size = (0, 48)
        self.header_bar = ActionBar()
        self.layout_header_view.add_widget(self.header_bar)
        self.root.add_widget(self.layout_header_view)

    def _layout_status(self):
        self.layout_status_view = BoxLayout()
        self.layout_status_view.size_hint = (1, None)
        self.layout_status_view.size = (0, 48)
        self.action_bar = ActionBar()
        self.layout_status_view.add_widget(self.action_bar)
        self.root.add_widget(self.layout_status_view)
