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

#Builder.load_file('style.kv')

class Grammar(GridLayout):
    def __init__(self, **kwargs):
        super(Grammar, self).__init__(**kwargs)
        #self.orientation = 'horizontal'
        self.cols=1
        self.top_grid=GridLayout()
        self.top_grid.cols=2
        self.top_grid.add_widget(Label(text="Name"))
        self.name=TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(text="Email"))
        self.email=TextInput(multiline=False)
        self.top_grid.add_widget(self.email)
        self.label=Label(text="-")
        self.add_widget(self.label)
        self.login=Button(text="Login")
        self.login.bind(on_press=self.press)
        self.add_widget(self.login)
    def press(self,instance):
        name=self.name.text
        email=self.email.text
        print(f'votre nom est {name} et votre email est {email}')
        self.label.text=f'votre nom est {name} et votre email est {email}'
        self.name.text=""
        self.email.text=""


class Main(App):
    def build(self):
        return Grammar()

if __name__ == "__main__":
    Main().run()
