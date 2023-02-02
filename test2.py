import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('style.kv')

class Gramar(GridLayout):
    def __init__(self, **kwargs):
        super(Gramar, self).__init__(**kwargs)
        pass
        
    def press(self,instance):
        name=self.name.text
        email=self.email.text
        print(f'votre nom est {name} et votre email est {email}')
        self.label.text=f'votre nom est {name} et votre email est {email}'
        self.name.text=""
        self.email.text=""


class Main(App):
    def build(self):
        return Gramar()

if __name__ == "__main__":
    Main().run()
