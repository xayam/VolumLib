from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.splitter import Splitter
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from volum.model.config import Config


class TableDesc(TabbedPanelItem):
    table_resulter: MDDataTable = None
    panel_description: Button = None

    def __init__(self, text):
        TabbedPanelItem.__init__(self, text=text)
        self.title = text
        self.background_normal = \
            Config.BG_STYLE_NORMAL["Dark"]
        self.background_down = \
            Config.BG_STYLE_DOWN["Dark"]

    def init(self):
        box_layout = BoxLayout(orientation="vertical")
        self.table_resulter = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30), self.sort_on_signal),
                ("Status", dp(30), self.sort_on_signal),
                ("Signal Name", dp(60), self.sort_on_signal),
                ("Severity", dp(30), self.sort_on_signal),
                ("Stage", dp(30), self.sort_on_signal),
                ("Schedule", dp(30), self.sort_on_schedule),
                ("Team Lead", dp(30), self.sort_on_team),
            ],
            row_data=[
                         (
                             "1",
                             ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                             "Astrid: NE shared managed",
                             "Medium",
                             "Triaged",
                             "0:33",
                             "Chase Nguyen",
                         ),
                         (
                             "2",
                             ("alert-circle", [1, 0, 0, 1], "Offline"),
                             "Cosmo: prod shared ares",
                             "Huge",
                             "Triaged",
                             "0:39",
                             "Brie Furman",
                         ),
                         (
                             "3",
                             (
                                 "checkbox-marked-circle",
                                 [39 / 256, 174 / 256, 96 / 256, 1],
                                 "Online",
                             ),
                             "Phoenix: prod shared lyra-lists",
                             "Minor",
                             "Not Triaged",
                             "3:12",
                             "Jeremy lake",
                         ),
                     ] * 10,
            sorted_on="Schedule",
            sorted_order="ASC",
            rows_num=20,
            elevation=20,
        )
        self.table_resulter.bind(on_row_press=self.on_row_press)
        self.table_resulter.bind(on_check_press=self.on_check_press)

        self.panel_description = Button()

        splitter = Splitter(sizable_from="top")
        splitter.size_hint = (1, None)
        splitter.size = (0, 250)
        splitter.min_size = '20pt'
        splitter.add_widget(self.panel_description)
        splitter.strip_size = '5pt'

        box_layout.add_widget(self.table_resulter)
        box_layout.add_widget(splitter)

        self.add_widget(box_layout)

    def on_row_press(self, instance_table, instance_row):
        """Called when a table row is clicked."""
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        """Called when the checkbox in the table row is checked."""
        print(instance_table, current_row)

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda x: x[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda x: sum(
                    [
                        int(x[1][-2].split(":")[0]) * 60,
                        int(x[1][-2].split(":")[1]),
                    ]
                ),
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda x: x[1][-1]))
