import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

kivy.require('1.9.0')


class Nicetyfarm(App):

    def build(self):
        return BoxLayout()


if __name__ == "__main__":
    Nicetyfarm().run()
