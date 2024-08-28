from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("test.kv")


class NotTest(BoxLayout):
    pass


class NotTestApp(App):
    def build(self):
        return NotTest()


NotTestApp().run()
