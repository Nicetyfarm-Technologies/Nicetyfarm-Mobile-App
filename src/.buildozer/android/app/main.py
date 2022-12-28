import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

# kivy.require('1.9.0')


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass

        
class DashboardScreen(Screen):
    pass


class ScanCropScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('nicetyfarm.kv')
   
        
class NicetyfarmMainApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    NicetyfarmMainApp().run()
