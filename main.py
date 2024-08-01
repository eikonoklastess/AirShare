from kivy.app import App, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class GridLayoutExemple(GridLayout):
    pass
    """
    counter = 0
    text = StringProperty("0")

    def counter_increment(self):
        self.counter += 1
        self.text = str(self.counter)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
    """


class MainWidget(Widget):
    pass


class AirShareApp(App):
    pass


AirShareApp().run()
