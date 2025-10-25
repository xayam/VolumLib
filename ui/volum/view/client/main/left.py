from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from volum.model.config import Config


class Left:

    def __init__(self, root: BoxLayout):
        self.root = root
        accordion = Accordion(orientation="vertical")
        self.accordion_authors_item = AccordionItem(title="Авторы")
        self.accordion_series_item = AccordionItem(title="Серии")
        self.accordion_genres_item = AccordionItem(title="Жанры")
        self.accordion_archives_item = AccordionItem(title="Архивы")
        self.accordion_tags_item = AccordionItem(title="Метки")
        self.accordion_search_item = AccordionItem(title="История")

        accordion.add_widget(self.accordion_authors_item)
        accordion.add_widget(self.accordion_series_item)
        accordion.add_widget(self.accordion_genres_item)
        accordion.add_widget(self.accordion_archives_item)
        accordion.add_widget(self.accordion_tags_item)
        accordion.add_widget(self.accordion_search_item)
        accordion.select(self.accordion_authors_item)
        for child in accordion.children:
            child.background_normal = Config.BG_STYLE_NORMAL["Dark"]
            child.background_down = Config.BG_STYLE_DOWN["Dark"]

        self.root.add_widget(accordion)
