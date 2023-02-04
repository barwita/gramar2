import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('style.kv')

class Gramar(GridLayout):
    def __init__(self, **kwargs):
        super(Gramar, self).__init__(**kwargs)
        pass
    
class Main(App):
    def build(self):
        return Gramar()

if __name__ == "__main__":
    Main().run()
