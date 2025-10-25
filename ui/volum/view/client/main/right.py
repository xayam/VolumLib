from kivy.uix.actionbar import ActionBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
# from kivymd.icon_definitions import md_icons

from volum.model.config import Config
from volum.view.client.main.resulter import Resulter
from volum.view.client.main.searches import Searches
from volum.view.client.main.readers import Readers


class Right:

    def __init__(self, root: BoxLayout):
        self.root = root
        # self._icons = list(md_icons.keys())[15:30]
        self._layout_search()
        self._layout_content()

    def _layout_search(self):
        self.layout_search_view = BoxLayout()
        self.layout_search_view.size_hint = (1, None)
        self.layout_search_view.size = (0, 48)
        self.search_bar = ActionBar()
        self.layout_search_view.add_widget(self.search_bar)
        self.root.add_widget(self.layout_search_view)

    def _layout_content(self):
        self.layout_content_view = BoxLayout()
        self.content_tabs = TabbedPanel()
        self.tab_resulter = Resulter()
        self.tab_searches = Searches()
        self.tab_readers = Readers()
        self.content_tabs.add_widget(self.tab_resulter)
        self.content_tabs.add_widget(self.tab_searches)
        self.content_tabs.add_widget(self.tab_readers)
        self.content_tabs.default_tab = self.tab_resulter
        self.content_tabs.tab_height = 20
        self.content_tabs.tab_pos = "right_top"
        self.content_tabs.background_image = Config.BG_STYLE_NORMAL["Dark"]

        self.layout_content_view.add_widget(self.content_tabs)
        self.root.add_widget(self.layout_content_view)


class Tab(MDFloatLayout, MDTabsBase):
    pass
