import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Sample2_Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Sample2_Layout,self).__init__()
        self.cols=2
        self.add_widget(Label(text="Student Name:"))
        self.s_name=TextInput(multiline=False)
        self.add_widget(self.s_name)

class Sample2(App):
    def build(self):
        return Sample2_Layout()

if __name__=="__main__":
    Sample2().run()