import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_file('style.kv')


class Gramar(Widget):
    def login(self):
        pass
    
class Main(App):
    def build(self):
        return Gramar()


if __name__ == '__main__':
    Main().run()
