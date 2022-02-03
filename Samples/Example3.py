from typing import Text
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Sample3_Layout(GridLayout):
    
    def __init__(self, **kwargs):
        
        super(Sample3_Layout,self).__init__()
        
        self.cols=2
        
        self.add_widget(Label(text="Student Name:"))
        self.s_name=TextInput(multiline=False)
        self.add_widget(self.s_name)
        
        self.add_widget(Label(text="Student Marks:"))
        self.s_marks=TextInput()
        self.add_widget(self.s_marks)
        
        self.add_widget(Label(text="Student Gender:"))
        self.s_gender=TextInput(multiline=False)
        self.add_widget(self.s_gender)

        self.press=Button(text="Click Me!")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
    
    def click_me(self, instance):
        print("Details entered successfully!")
        print(f"Name of student is {self.s_name.text}")
        print(f"Marks of student is {self.s_marks.text}")
        print(f"Gender of student is {self.s_gender.text}")


class Sample3(App):
    def build(self):
        return Sample3_Layout()

if __name__=="__main__":
    Sample3().run()