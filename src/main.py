import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

# kivy.require('1.9.0')
   
        
class Nicetyfarm(App):
    
    name = ObjectProperty(None)
    phone = ObjectProperty(None)
    
    def btn (self):
        name = self.name.text
        phone = self.phone.text
        # print("Name:" self.name, "Phone:" self.phone)

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    Nicetyfarm().run()
