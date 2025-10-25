from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class LoaderScreen(Screen):

    def __init__(self, name):
        Screen.__init__(self)
        self.name = name
        button1 = Button(text="Goto settings", on_press=self.on_press)
        button2 = Button(
            text="QUit",
        )
        layout = BoxLayout()
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)

    def on_press(self, _):
        self.manager.current = "settings"
