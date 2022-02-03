import kivy
from kivy.app import App
from kivy.uix.label import Label

class Sample1(App):
    def build(self):
        return Label(text="This is a sample app!")

if __name__=="__main__":
    Sample1().run()