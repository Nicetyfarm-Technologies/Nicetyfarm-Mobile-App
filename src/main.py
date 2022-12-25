import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# kivy.require('1.9.0')

class Mygrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    
    def btn(self):
        print("Name:", self.name.text, "Email:", self.email.text)
        self.name.text = ""
        self.email.text = ""
    
        
class Nicetyfarm(App):

    def build(self):
        return Mygrid()


if __name__ == "__main__":
    Nicetyfarm().run()
