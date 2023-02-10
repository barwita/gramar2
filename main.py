import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file('style.kv')


class Gramar(Widget):
    oracion=ObjectProperty(None)
    def analizar(self):
        self.oracion.text=""
    
class Main(App):
    def build(self):  
        Window.clearcolor=(1,1,1,1)     
        return Gramar()


if __name__ == '__main__':
    Main().run()
