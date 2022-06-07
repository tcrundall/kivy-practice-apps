"""
Codemy course:
https://www.youtube.com/watch?v=Prt_SKkZji8&ab_channel=Codemy.com

Relavant docs:
https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# Define our different screens
class FirstWindow(Screen):
    pass

    def on_press(self):
        print("pressed!")
        self.manager.screen = "second"


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Designate our .kv design file
kv = Builder.load_file('new_window.kv')


class AwesomeApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    AwesomeApp().run()
